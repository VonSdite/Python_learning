#设置猜拳的对象
import tkinter as tk
import random

#root表示窗口
#pos表示在窗口的位置
#flag表示是否被占用，无则用狗狗图显示
class Person:
	def __init__(self, root, pos, flag, name=""):
		self.temp = -1
		self.frame = tk.Frame(root)
		self.pos = pos
		self.name = name
		if flag:
			self.photo = tk.PhotoImage(file="Img/%s/0.gif" % self.pos)
		else:
			self.photo = tk.PhotoImage(file="Img/dog.gif")
		self.TextLabel = tk.Label(self.frame, text=name, font=("黑体", 15))
		self.Label = tk.Label(self.frame, image=self.photo)
		self.TextLabel.pack(pady=5)
		self.Label.pack()

	#框架的摆放
	def pack(self):
		if self.pos == "Left":
			self.frame.pack(side=tk.LEFT)
		elif self.pos == "Right":
			self.frame.pack(side=tk.RIGHT)
		elif self.pos == "Bottom":
			self.frame.pack(side=tk.BOTTOM)
		else:
			self.frame.pack()

	#胜利人的设置
	def win(self):
		self.temp = -1
		self.photo = tk.PhotoImage(file="Img/dog.gif")
		self.Label.configure(image=self.photo)

	#输的人的设置
	def loser(self):
		self.photo = tk.PhotoImage(file="Img/smile.gif")
		self.Label.configure(image=self.photo)

		