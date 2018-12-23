import tkinter as tk
import random

temp_down = 0
temp_left = 0
temp_right = 0
temp_top = 0

#设置窗口大小 并设置窗口位置
def center_window(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/3, (screenheight - height)/3)  
    root.geometry(size) 

def update_picture_top():
	global photo_top
	global temp_top
	temp_top = random.randint(0,2)
	pict_name = "../Img/Top/%d.gif" % temp_top
	photo_top = tk.PhotoImage(file=pict_name)
	theLabel_top.configure(image=photo_top)
	frame_top.after(180, update_picture_top)

def update_picture_down():
	global photo_down
	global temp_down
	temp_down = random.randint(0,2)
	pict_name = "../Img/Down/%d.gif" % temp_down
	photo_down = tk.PhotoImage(file=pict_name)
	theLabel_down.configure(image=photo_down)
	frame_down.after(180, update_picture_down)

def update_picture_left():
	global photo_left
	global temp_left
	temp_left = random.randint(0,2)
	pict_name = "../Img/Left/%d.gif" % temp_left
	photo_left = tk.PhotoImage(file=pict_name)
	theLabel_left.configure(image=photo_left)
	frame_left.after(180, update_picture_left)

def update_picture_right():
	global photo_right
	global temp_right
	temp_right = random.randint(0,2)
	pict_name = "../Img/Right/%d.gif" % temp_right
	photo_right = tk.PhotoImage(file=pict_name)
	theLabel_right.configure(image=photo_right)
	frame_right.after(180, update_picture_right)

def pause():
	pass

root = tk.Tk()
center_window(root, 800, 660)

frame_top = tk.Frame(root)
frame_down = tk.Frame(root)
frame_left = tk.Frame(root)
frame_right = tk.Frame(root)
frame_button = tk.Frame(root)

photo_top = tk.PhotoImage(file="../Img/Top/0.gif")
theLabel_top = tk.Label(
	frame_top,
	image=photo_top)
theLabel_top.pack()
update_picture_top()

photo_left = tk.PhotoImage(file="../Img/Left/0.gif")
theLabel_left = tk.Label(
	frame_left,
	image=photo_left)
theLabel_left.pack()
update_picture_left()


photo_right = tk.PhotoImage(file="../Img/Right/0.gif")
theLabel_right = tk.Label(
	frame_right,
	image=photo_right)
theLabel_right.pack()
update_picture_right()


photo_down = tk.PhotoImage(file="../Img/Down/0.gif")
theLabel_down = tk.Label(
	frame_down,
	image=photo_down)
theLabel_down.pack()
update_picture_down()

theButton = tk.Button(frame_button, text="暂停", command=pause)
theButton.pack()

frame_top.pack()
frame_left.pack(side=tk.LEFT)
frame_right.pack(side=tk.RIGHT)
frame_button.pack(side=tk.BOTTOM)
frame_down.pack(side=tk.BOTTOM)

root.mainloop()