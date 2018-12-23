import requests
import time
import re
from bs4 import BeautifulSoup
from proxy import *

# ip_list = get_ip_list()  # 获取代理ip列表

# 用途:用于打开网页
# --------------------
# 按需使用代理，要使用代理则将下面的注释更换
# 自动设置了代理ip，防爬虫被禁
# --------------------
def openURL(url, interval=5):
    headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    # proxies = get_proxy(ip_list)
    # page = requests.get(url, headers=headers, proxies=proxies)
    # print(time.strftime('%F %X'))
    page = requests.get(url, headers=headers)
    # print(time.strftime('%F %X'))
    soup = BeautifulSoup(page.text, 'lxml')
    time.sleep(interval)
    return soup


class Question(object):
    """docstring for Question"""
    # 问题列表

    def __init__(self, url, num):
        super(Question, self).__init__()
        # 获取的问题数量，最好是20的倍数
        self.num = num

        # Programming & Design区的网址
        self.url = url

        # 问题列表以及问题链接
        self.questions = dict()

    def sava_data(self, file, data):
        with open(file, 'a') as f:
            for key in data:
                f.write(str(key) + ': ')
                f.write('\n')
                for k in data[key]:
                    f.write(k + ': ' + data[key][k])
                    f.write('\n')

    def get_questions(self):
        questions = dict()
        for page in range(0, self.num, 20):
            url = self.url % page
            soup = openURL(url, interval=0)

            num = page + 1
            questions.clear()
            for question in soup.find_all('li', class_='ya-discover-tile ya-discover-tile-qn Bfc P-14 Bdbx-1g Bgc-w'):
                link = 'https://answers.yahoo.com/question/index?qid=' + \
                    question['data-id']
                text = question.find_all(
                    'a', class_='Fz-14 Fw-b Clr-b Wow-bw title')[0].text
                answer_num = question.find_all(
                    'div', class_='Clr-888 Fz-12 Lh-18')[0].text
                answer_num = re.search(r'\d+', answer_num).group(0)
                tmp = dict()
                tmp['question'] = text
                tmp['answerNum'] = answer_num
                tmp['href'] = link
                print('Try to obtain the users of the %d question' % num)

                self.questions[num] = tmp
                questions[num] = tmp
                num += 1
            print('***************************************')  # 每爬完一次问题，分割一下
            self.sava_data('Question.txt', questions)


class Answer(object):
    """docstring for Answer"""
    # 回答页面

    def __init__(self, question, num):
        super(Answer, self).__init__()
        self.question = question
        self.num = num
        self.answers = dict()

    def sava_data(self, file, data):
        with open(file, 'a') as f:
            for key in data:
                f.write(str(key) + ': ')
                f.write('\n')
                for k in data[key]:
                    f.write(k + ': ' + data[key][k])
                    f.write('\n')

    def get_answer(self):

        for num in range(0, self.num + 1):
            answer = dict()
            answer['question'] = self.question[num]['question']
            answer['href'] = self.question[num]['href']
            soup = openURL(answer['href'], interval=5)
            try:
                Quser = soup.find_all(
                    'a', class_='Clr-b')[3].img['alt']
                answer['asker'] = Quser
            except:
                answer['asker'] = '-1'

class User(object):
    """docstring for User"""
    def __init__(self, arg):
        super(User, self).__init__()
        self.arg = arg
        

if __name__ == '__main__':
    # Programming & Design区的基址
    url = 'https://answers.yahoo.com/dir/index/discover?after=pv%d%%7Ep%%3A0&sid=396545663'

    # question = Question(url, 20)
    # question.get_questions()

