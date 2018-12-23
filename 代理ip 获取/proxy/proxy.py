# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/

from bs4 import BeautifulSoup
import requests
import random
import pickle


def get_ip_list(num=1):
    # 默认只爬一页

    ip_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    for i in range(1, num + 1):
        url = 'http://www.xicidaili.com/nn/%d' % i
        # print("爬取第%d页...." % i)
        web_data = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append('http://' + tds[1].text + ':' + tds[2].text)
    return ip_list

if __name__ == '__main__':
    ip_list = get_ip_list(num=5)

    # 用pickle保存下来
    with open("save.pkl", "wb") as f:
        pickle.dump(ip_list, f)


# 使用方法 web_data = requests.get(url, headers=headers, proxies=proxies)


# 获取ip方法
# def get_random_ip(ip_list):
#     proxy_ip = random.choice(ip_list)
#     proxies = {'http': proxy_ip}
#     return proxies


# def get_proxy(ip_list):
#     proxies = get_random_ip(ip_list)
#     return proxies
