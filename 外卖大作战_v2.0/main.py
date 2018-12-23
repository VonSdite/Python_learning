#主程序
from Person import *
from SetWindows import *
from screen_capture import *
from SendMessage import *
import easygui as e
import copy


def main():
	#一开始不要看这个函数
	#它是结束函数
	def end():
		#截屏
		nonlocal x, y, width, height
		window_capture('Img/Res/', srcbmp=[x, y, width+15, height-10])
		#发送信息到微信群中
		send()
		root.destroy()

	#暂停按钮控制
	start = True
	def started(person, win_person):
		#允许继续出拳
		nonlocal start
		start = True

		#将赢的人换成狗狗
		for w in win_person:
			w.win()

		#只剩一个人的话，这个人换成微笑
		#否则，继续出拳
		if len(person) == 1:
			person = list(person)
			person[0].loser()

			theEndResult.configure(text="就是你了:\n\n"+person[0].name)
			#更新按钮功能
			theButton.configure(text="不服？再来一次<(￣︶￣)↗[GO!]", command = end)
		else:	
			for p in person:
				update_picture(p)

			#更新按钮功能
			theButton.configure(command = pause)


	#暂停功能
	def pause():
		nonlocal start
		start = False
		person = set()
		win_person = set()
		temp = set()

		#下面的判断是判断这个人是否赢了或者有无参加本次外卖
		#赢了，或者无参加的话，不被加入到person集合中
		if top.temp != -1:
			temp.add(top.temp)
			person.add(top)

		if left.temp != -1:
			temp.add(left.temp)
			person.add(left)

		if right.temp != -1:
			temp.add(right.temp)
			person.add(right)

		if bottom.temp != -1:
			temp.add(bottom.temp)
			person.add(bottom)

		#只有两种出拳，则必有人赢
		#把赢的人放到win_person集合中，
		#并在person中删除赢的人
		if len(temp) == 2:
			temp = list(temp)
			tm = copy.copy(person)			
			#由于删除赢的人会改变person大小，所以要copy一个person来辅助查找

			if temp[0] == 0:
				if temp[1] == 1:
					for i in tm:
						if i.temp == 1:
							win_person.add(i)
							person.remove(i)
				else:
					for i in tm:
						if i.temp == 0:
							win_person.add(i)
							person.remove(i)
			if temp[0] == 1:
				for i in tm:
					if i.temp == 2:
						win_person.add(i)
						person.remove(i)

		#更新按钮功能
		theButton.configure(command = lambda:started(person, win_person))

	#更新图片
	def update_picture(self):
		#start用于判断是否出拳
		nonlocal start
		if start:
			self.temp = random.randint(0,2)
			pict_name = "Img/%s/%d.gif" % (self.pos, self.temp)
			self.photo = tk.PhotoImage(file=pict_name)
			self.Label.configure(image=self.photo)
			self.frame.after(200, lambda:update_picture(self))

	#选择参加外卖的人
	def choice_people():
		msg = "\n\n\t\t( ‵▽′)ψ  谁叫了外卖"
		title = "外卖大作战!(°ー°〃)_v2.0"
		choices = ["大佬杰", "大佬忠", "大佬A", "大佬王"]

		choice = e.multchoicebox(msg, title, choices)
		return choice

	#拿外卖的待选人员
	pending_person = choice_people()
	try:
		length = len(pending_person)
	
	except:
		length = 2
		
	#判断是不是只选了一个人
	#若只选了一个人，程序往下走
	while length == 1:
		e.msgbox(
			"请确保有两个人以上叫了外卖!!  (｀へ´)", 
			"外卖大作战!(°ー°〃)_v2.0", 
			ok_button="好的....")
		pending_person = choice_people()
		length = len(pending_person)

	#窗口的设置
	root = tk.Tk()
	root.wm_title("外卖大作战!(°ー°〃)_v2.0")	#窗口的标题

	width = 740
	height = 750
	screenwidth = root.winfo_screenwidth()  
	screenheight = root.winfo_screenheight()
	x = int((screenwidth - width)/3)
	y = int((screenheight - height)/3)
	#窗口大小和初始位置的设置
	center_window(root, x, y, width, height)			

	#每个人的出拳
	#由于至少有两个人参与，所以窗口顶部与左侧开始均被占用
	top = Person(root, "Top", flag=True, name=pending_person[0])
	update_picture(top)

	left = Person(root, "Left", flag=True, name=pending_person[1])
	update_picture(left)

	#如果有三个人话，窗口右侧被占用
	#否则显示狗狗
	if length >= 3:
		right = Person(root, "Right", flag=True, name=pending_person[2])
		update_picture(right)
	else:
		right = Person(root, "Right", flag=False)

	#如果有四个人话，窗口底部被占用
	#否则显示狗狗
	if length == 4:
		bottom = Person(root, "Bottom", flag=True, name=pending_person[3])
		update_picture(bottom)
	else:
		bottom = Person(root, "Bottom", flag=False)


	#暂停按钮
	#用于暂停出拳
	button_frame = tk.Frame(root)
	theButton = tk.Button(
			button_frame, 
			text="决定就是你了 <(￣︶￣)>", 
			font=("黑体", 13),
			command=pause
			)
	theButton.pack(pady=10)

	ResultFrame = tk.Frame(root)
	theEndResult = tk.Label(ResultFrame, text ="", font=("黑体", 25))
	theEndResult.pack()

	top.pack()
	left.pack()
	right.pack()
	button_frame.pack(side=tk.BOTTOM)
	bottom.pack()
	ResultFrame.pack(side=tk.BOTTOM, pady=80)

	root.mainloop()

if __name__ == '__main__':
	main()