import requests
import time
import re
from proxy import *
from bs4 import BeautifulSoup

ip_list = get_ip_list()  # 获取代理ip列表


class Yahoo(object):
    """docstring for Yahoo"""

    # 初始化
    def __init__(self, url, num):
        super(Yahoo, self).__init__()
        self.num = num 				# 获取的问题数量，最好是20的倍数
        self.url = url 				# 编程区的网址
        self.questions = list()		# 获取的问题标题列表
        self.links = list()			# 获取的问题的链接
        self.Quser = list()			# 提出问题的用户名
        self.Auser = list()			# 回答问题的用户名

    # 用途:用于打开网页
    # --------------------
    # 按需使用代理，要使用代理则将下面的注释更换
    # 自动设置了代理ip，防爬虫被禁
    # --------------------
    def openURL(self, url, interval=5):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
        }
        # proxies = get_proxy(ip_list)
        # page = requests.get(url, headers=headers, proxies=proxies)
        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.text, 'lxml')
        time.sleep(interval)
        return soup

    # 用途:获取问题列表, 以及链接
    # --------------------
    # 传入的url_base是基址
    # questions_NUM是要获取的问题数量
    # --------------------
    def get_questions(self):
        for page in range(0, self.num, 20):
            num = page + 1
            url = self.url % page
            soup = self.openURL(url)

            for question in soup.find_all('a', class_='Fz-14 Fw-b Clr-b Wow-bw title'):
                link = 'https://answers.yahoo.com' + question['href']
                print('Try to obtain the users of the %d question' % num)
                self.get_user(link, question)
                num += 1
            print('***************************************')  # 每爬完20个问题，分割一下
        # print(len(self.questions))		#显示实际爬到问题数量

    # 用途:获取问题中 提问的用户，回答的用户
    # --------------------
    # 剔除匿名提问者
    # 解决某个问题可能需要翻页
    # --------------------
    def get_user(self, url, question):
        soup = self.openURL(url)
        flag = True
        # 捕获的异常
        # 由于提问者匿名提问， 所以会导致异常
        # 捕获到异常跳过，即可剔除匿名提问者
        try:
            Quser = soup.find_all(
                'a', class_='Clr-b')[3].img['alt']
            self.Quser.append(Quser)

            Auser = [user.text for user in soup.find_all(
                'a', class_='uname Clr-b')]
            try:
                page = soup.find_all(
                    'div', class_="D-ib Py-7 Px-10 Bdx-1g Fw-13 Bgc-page ")[-2].text
                for begin in range(2, int(page) + 1):
                    URL = url + '&page=%d' % begin
                    soup = self.openURL(URL)
                    Auser += [user.text for user in soup.find_all(
                        'a', class_='uname Clr-b')]
            except:
                pass
            self.Auser += Auser

            # 由于可能提问者匿名，导致这个问题应该要被过滤
            # 所以在此处才记录问题内容
            self.questions.append(question.text)
            self.links.append(url)

            print('Obtain successfully!')
            flag = False
        except:
            if flag:
                print('Obtain failed...')

    def run(self):
        print('System start!')
        self.get_questions()
        print(len(self.questions))
        print(self.Quser)
        print(self.Auser)


if __name__ == '__main__':
    url = 'https://answers.yahoo.com/dir/index/discover?after=pv%d%%7Ep%%3A0&sid=396545663'  # 编程区网址

    test = Yahoo(url, 20)  # 第一个参数是网址， 第二个是爬取的question的数目(数目要为20的倍数)
    test.run()
