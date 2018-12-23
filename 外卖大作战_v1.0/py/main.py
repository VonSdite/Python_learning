import tkinter as tk
import random
import time
import sys
import easygui as e

def main():
	import select as s
	#拿外卖 待选人员
	pending_person = s.choice_people()
	length = len(pending_person)
	while length == 1:
		e.msgbox(
			"请确保有两个人以上叫了外卖!!  (｀へ´)", 
			"外卖大作战!(°ー°〃)_v1.0", 
			ok_button="好的....")
		pending_person = s.choice_people()
		length = len(pending_person)
	flag_pause = False
	cnt = 0

	#刷新滚动人员的函数
	def update_theLabel():
		nonlocal flag_pause
		nonlocal length
		if not flag_pause:
			temp = random.randint(0, length-1)
			theLabel.configure(text=pending_person[temp])
			frame1.after(60, update_theLabel)	

	#实现图片的动态效果
	def update_picture():
		nonlocal cnt
		nonlocal photo
		cnt += 1
		cnt %= 8
		picture_name = "../Img/Cry%d.gif" % cnt
		photo = tk.PhotoImage(file=picture_name)
		imageLabel.configure(image=photo)
		frame1.after(50, update_picture)	

	#设置时钟刷新
	def clock():
		current = time.strftime("%F %H:%M:%S")
		timeText.configure(text=current)
		root.after(1000, clock)

	#结束， 重新开始
	def end():
		root.destroy()

	#停止滚动
	def pause():
		nonlocal flag_pause
		flag_pause = True
		theButton.configure(
			text="重新开始<(￣︶￣)>",
			command=end
			)

	#设置窗口大小 并设置窗口位置
	def center_window(root, width, height):  
	    screenwidth = root.winfo_screenwidth()  
	    screenheight = root.winfo_screenheight()  
	    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/3, (screenheight - height)/3)  
	    root.geometry(size)  

	#窗体创建
	root = tk.Tk()
	#窗体的名字
	root.wm_title("外卖大作战!(°ー°〃)_v1.0")
	center_window(root, 900, 530)

	frame1 = tk.Frame(root)			#用于放置滚动的人员和图片
	frame2 = tk.Frame(root)			#用于放置暂停按钮
	frame3 = tk.Frame(root)			#放置时钟

	#第一部分，滚动的成员表
	theLabel = tk.Label(frame1, text="", font=("楷体", 150))
	theLabel.pack()
	update_theLabel()

	photo = tk.PhotoImage(file="../Img/Cry0.gif")
	imageLabel = tk.Label(frame1, image=photo)
	imageLabel.pack()
	update_picture()

	frame1.pack()

	#第二部分，暂停按钮
	theButton = tk.Button(
		frame2, 
		text="决定就是你了 <(￣︶￣)>", 
		font=("黑体", 13),
		command=pause
		)
	theButton.pack(pady=5)

	frame2.pack()

	#第三部分， 放置时钟
	timeText = tk.Label(
		frame3,
		text="", 
		font=("Helvetica", 13)
		)
	timeText.pack()
	clock()

	frame3.pack(side=tk.RIGHT)

	root.mainloop()

if __name__ == '__main__':
	main()