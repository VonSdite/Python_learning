import pyexcel
from get_name import *
from make_schedule import *

file_name = get_file()						# 获取当前目录下所有'/File/.xls'文件
final = init_sheet(file_name[0]) 			# 存储最终的空课表
for each in file_name:
	sheet = pyexcel.get_sheet(file_name=each)		# 打开课表
	sheet = deal(sheet, each)						# 制成个人空课表
	final = merge(final, sheet)						# 合并空课表

final = calc(final)                         # 计算每个时间段人数
final.save_as('final.xls')