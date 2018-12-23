#coding=utf-8
import itchat

# 获取好友列表
# 保存在save.txt中

def lg():
	print('Start to login....')

def ec():
	print('Exit...')

if __name__ == '__main__':
	itchat.auto_login(loginCallback=lg, exitCallback=ec, hotReload=True)
	friends = itchat.get_friends()
	print('好友数: '+str(len(friends)-1))
	with open('save.txt', 'w', encoding='utf-8') as f:
		for person in friends:
			for key in person:
				f.write(key)
				f.write(': ')
				f.write(str(person[key]))
				f.write('\n')
			f.write('********************************************\n')
	itchat.logout()