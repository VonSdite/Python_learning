import urllib.request as u
from bs4 import BeautifulSoup
import urllib.parse as p
import re

def open_url(url):
	req = u.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
	response = u.urlopen(req)
	html = response.read()
	return html

def save_address():
	for i in range(5, 0, -1):
		url = "http://blog.fishc.com/category/winsdk/page/%d" % i

		html = open_url(url)
		soup = BeautifulSoup(html, "lxml")

		for link in soup.find_all('h2'):
			tmp = open_url(link.a['href']).decode('utf-8')
			address = re.findall(r'(http://pan.baidu.com/.+?)"', tmp)[0]
			password = re.findall(r'密码：....', tmp)[0][3:]
			print(link.a.text + ": " + address + " "+ password)

save_address()