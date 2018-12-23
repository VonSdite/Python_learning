#发送信息到微信群
import itchat

def send():
	itchat.auto_login(hotReload=True)

	room_name = itchat.search_chatrooms(name='3607咸鱼聚集')[0]['UserName']

	itchat.send("猜拳结果:", room_name)
	itchat.send("@img@%s" % "Img/Res/Result.jpg", room_name)

	itchat.logout()
	itchat.run()
	itchat.dump_login_status()