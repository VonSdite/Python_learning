from get_target import *
import itchat
import time


def lc():
    print('Successful login')


def ec():
    print('Exit')

# user是要发送给的人的名单
def send_Message(user):
    users = list()
    for person in user:
        # 异常捕获是因为微信可能没加这个人
    	try:
    		tmp = itchat.search_friends(name='郑棉鑫')[0]['UserName']
    		users.append(tmp)
    	except:
    		print('找不到: '+person)
    content = '那我是 弱智了。。。 x'
    # print(len(users))
    for person in users:
        itchat.send(content, person)

itchat.auto_login(loginCallback=lc, exitCallback=ec, hotReload=True)
for i in range(10000, 0, -1):
    content = '那我是 弱智了。。。 x%d' % i
    itchat.send(content, itchat.search_friends(name='郑棉鑫')[0]['UserName'])
    
# rest = get_rest()
# send_Message(user=rest)

itchat.logout()
