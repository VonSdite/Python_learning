import itchat
import time

def lc():
    print('Successful login')


def ec():
    print('Exit')

itchat.auto_login(loginCallback=lc, exitCallback=ec, hotReload=True)
for i in range(10000, 0, -1):
    content = '那我是 弱智了。。。 x%d' % i
    itchat.send(content, itchat.search_friends(name='郑棉鑫')[0]['UserName'])
    time.sleep(5)


itchat.logout()