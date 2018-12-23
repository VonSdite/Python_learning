import urllib.request as u
import re
from bs4 import BeautifulSoup

def main():
    url = 'http://baike.baidu.com/view/284853.htm'

    req = u.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = u.urlopen(url)

    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    for each in soup.find_all(href=re.compile("view")):
        print(' -> '.join([each.text, ''.join(["https://baike.baidu.com", each['href']])]))

if __name__ == "__main__":
    main()
