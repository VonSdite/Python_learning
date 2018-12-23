from selenium import webdriver
import re
import urllib.request as u
from Ip import *

url = 'http://www.chsi.com.cn/cet/query'

def get(key="", name=""):
	driver = webdriver.PhantomJS(executable_path='D:/python/phantomjs-2.1.1-windows/bin/phantomjs.exe')

	# proxy_support = u.ProxyHandler(get_random_ip())
	# opener = u.build_opener(proxy_support)
	# opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
	# u.install_opener(opener)

	driver.get(url)
	driver.find_element_by_id('zkzh').send_keys(key)
	driver.find_element_by_id('xm').send_keys(name)
	driver.find_elements_by_tag_name('form')[1].submit()

	print(driver.find_element_by_xpath('//tr[3][1]').text)
	print(driver.find_element_by_xpath('//tr[6][1]').text)
	print(driver.find_element_by_xpath('//tr[7][1]').text)
	print(driver.find_element_by_xpath('//tr[8][1]').text)
	print(driver.find_element_by_xpath('//tr[9][1]').text)
						


key = "**********"
name = "****"

get(key, name)

