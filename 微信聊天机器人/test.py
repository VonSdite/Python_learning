import requests, json
import itchat
from itchat.content import *

#start用于之后管理员来开启和关闭自动回复系统
#True 为开启自动回复系统
#Flase 为关闭自动回复系统
start = True

@itchat.msg_register([PICTURE])
def simple_reply(msg):
	global set_friends
	global start

	#获取发送消息过来的用户UserName值
	username = msg['FromUserName']

	if start:
		if username not in set_friends:
			return ""
		else:
			return "狗子: 不要发图片, 我看不懂[微笑]"
	else:
		return ""

@itchat.msg_register([TEXT])
def text_reply(msg):
	global set_friends
	global flag
	global admin
	global start

	#获取发送消息过来的用户UserName值
	username = msg['FromUserName']

	#判断用户是不是管理员
	if username == admin:
		#判断管理员是否发出
		#开启自动回复系统的信号  open
		#关闭自动回复系统的信号  close
		#重启自动回复系统的信号  restart
		#退出系统的信号  quit
		#
		#重启系统和开启系统的区别在于:
		#开启是保留上次用户关闭自动回复的状态以及是否已经发送提醒信息
		#重启则是全部重新启动
		if "restart" == msg['Text']:
			start = False
		elif "open" == msg['Text']:
			start = True
			return ""
		elif "close" == msg['Text']:
			start = False
		elif "quit" == msg['Text']:
			itchat.logout()

	#判别系统是开启还是关闭
	if start:
		#第一次发送提醒信息
		if username in flag:
			itchat.send('狗子: 可输入"关闭自动回复"来关闭自动回复功能[微笑]\n输入"开启自动回复"以开启自动回复功能[色]', username)
			flag.remove(username)

		#判断用户是否要开启或者关闭自动回复
		if '开启自动回复' in msg['Text']:
			set_friends.add(username)
			return '狗子: 自动回复已开启'
		elif '关闭自动回复' in msg['Text']:
			set_friends.remove(username)
			return '狗子: 自动回复已关闭'

		#用户关闭自动回复
		#返回空字符串
		if username not in set_friends:
			return ""

		#用户自动回复状态处于开启状态
		
		KEY = 'b74895fe92fe426ea5f4839212dcd995'
		#此处去图灵机器人官网注册个账号，然后创建个机器人，把机器人的key复制到这里
		
		url = 'http://www.tuling123.com/openapi/api'

		info = msg['Text']
		req_info = info.encode('utf-8')
		query = {'key': KEY, 'info': req_info}
		headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

		r = requests.get(url, params=query, headers=headers)
		res = r.text

		response = '狗子: ' + json.loads(res).get('text').replace('<br>', '\n') 
		return response

	#系统关闭状态
	else:
		#判断是否要重启
		if "restart" == msg['Text']:
			it = itchat.get_friends()
			set_friends = set()
			for i in it:
				set_friends.add(i['UserName'])
			flag = set_friends.copy()
			start = True
			
		#处于关闭状态
		#返回空字符串
		return ""
	
#登录微信	
itchat.auto_login(hotReload = True)

#获取好友列表
#返回的是一个好友列表
#列表中每个元素是字典, 即每个好友的所有信息的字典
it = itchat.get_friends()

#获取管理员'Sdite'的 UserName的值
#用于后边开启和关闭系统
admin = itchat.search_friends(name='棉三金')[0]['UserName']

#建立好友UserName集合
#用于后边好友关闭和开启自动回复功能
set_friends = set()
for i in it:
	set_friends.add(i['UserName'])

#copy一份好友UserName集合
#发送提醒信息
#用于第一次提醒好友可以通过
#'关闭自动回复'和'开启自动回复'实现相应功能
flag = set_friends.copy()

itchat.run()
itchat.dump_login_status()
