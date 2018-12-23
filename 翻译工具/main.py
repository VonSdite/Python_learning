import tkinter as tk
import urllib.request as u
import urllib.parse as p
import json as j
import time as t

#设置窗口大小 并设置窗口位置
def center_window(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/3, (screenheight - height)/3)  
    root.geometry(size)  

def translation():
	global theButton
	global theInput
	global theList

	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

	data = {}
	data['type'] = 'AUTO'
	data['i'] = theInput.get()
	data['doctype'] = 'json'
	data['xmlVersion'] = '1.8'
	data['keyfrom'] = 'fanyi.web'
	data['ue'] = 'UTF-8'
	data['action'] = 'FY_BY_CLICKBUTTON'
	data['typoResult'] = 'true'	
	data = p.urlencode(data).encode('utf-8')

	req = u.Request(url, data)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 Safari/537.36')
	response = u.urlopen(req)	
	html = j.loads(response.read().decode('utf-8'))	

	theList.insert(0, html['translateResult'][0][0]['tgt'])
	
	theInput.destroy()
	theButton.destroy()
	theInput = tk.Entry(frame1, text="input", width=43, font=("黑体", 18))
	theButton = tk.Button(frame1, text="翻译", command=translation)

	theInput.pack(side=tk.LEFT, padx=5)
	theButton.pack(side=tk.RIGHT, padx=8)


root = tk.Tk()
root.wm_title("翻译小工具")
center_window(root, 720, 460)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

theInput = tk.Entry(frame1, text="input", width=43, font=("黑体", 18))
theButton = tk.Button(frame1, text="翻译", command=translation)


theList = tk.Listbox(frame2, height=18, width=45, font=("黑体", 18))
sl = tk.Scrollbar(frame2)
sl.pack(side=tk.RIGHT, fill = tk.Y) 
theList['yscrollcommand'] = sl.set  
sl['command'] = theList.yview

theInput.pack(side=tk.LEFT, padx=5)
theButton.pack(side=tk.RIGHT, padx=8)
theList.pack()

frame1.pack(pady=3)
frame2.pack(
	side=tk.LEFT,
	pady=10,
	padx=5)

root.mainloop()