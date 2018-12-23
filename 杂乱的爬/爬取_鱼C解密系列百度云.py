import urllib.request as u
from bs4 import BeautifulSoup
import urllib.parse as p
import re
import webbrowser

def open_url(url):
	req = u.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
	response = u.urlopen(req)
	html = response.read()
	return html

def save_address():
	# url = 'http://blog.fishc.com/category/base' # 基础篇
		
	# url = 'http://blog.fishc.com/category/pe/page/' # 系统篇
	# for i in range(2, 0, -1):
	# 	url = url + str(i)
		
	# url = 'http://blog.fishc.com/category/debug/page/' # 调试篇
	# for i in range(3, 0, -1):
	# 	url = url + str(i)	
	
	# url = 'http://blog.fishc.com/category/unpack' # 脱壳篇

	url = 'http://blog.fishc.com/category/tool' # 工具篇
	html = open_url(url)
	soup = BeautifulSoup(html, "lxml")
	for link in soup.find_all('h2'):
		tmp = open_url(link.a['href']).decode('utf-8')
		address = re.findall(r'(http://pan.baidu.com/.+?)"', tmp)[0]
		# webbrowser.open(address, new=0, autoraise=True)
		password = re.findall(r'密码：....', tmp)[0][3:]
		print(link.a.text + ": " + address + " "+ password)

save_address()