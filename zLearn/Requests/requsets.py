import requests
import json 

r = requests.get(url='http://www.baidu.com')    # 最基本的GET请求
print(r.status_code)    # 获取返回状态


r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
print(r.url)
print(r.text)   #打印解码后的返回数据




# 不但GET方法简单，其他方法都是统一的接口样式！
requests.get('https://github.com/timeline.json') 	#GET请求
requests.post('http://httpbin.org/post') 			#POST请求
requests.put('http://httpbin.org/put') 				#PUT请求
requests.delete('http://httpbin.org/delete') 		#DELETE请求
requests.head('http://httpbin.org/get') 			#HEAD请求
requests.options('http://httpbin.org/get') 			#OPTIONS请求

# 带参数的请求实例：
#
# GET参数实例
requests.get('http://www.dict.baidu.com/s', params={'wd': 'python'})    

# POST参数实例
requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})
# post发送json实例
requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))



#定制header
data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 
r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)



# 使用requests方法后，会返回一个response对象，其存储了服务器响应的内容，如上实例中已经提到的 r.text、r.status_code……
# 获取文本方式的响应体实例：当你访问 r.text 之时，会使用其响应的文本编码进行解码，并且你可以修改其编码让 r.text 使用自定义的编码进行解码。

r = requests.get('http://www.itwhy.org')
print(r.text, '\n{}\n'.format('*'*79), r.encoding)

r.encoding = 'GBK'
print(r.text, '\n{}\n'.format('*'*79), r.encoding)