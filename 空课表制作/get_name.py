import os
import glob

def get_file():
	path = os.getcwd()					# 获取当前路径
	path += '/File'

	file = glob.glob(path+'/*.xls')		# 获取当前路径下所有.xls文件名
	
	########################################
	# 运用os库的方法
	# file = list()
	# # 获取当前路径下所有.xls文件名
	# for each in os.listdir(path):
	# 	# os.path.splitext作用是将文件名分成文件名和扩展名
	# 	if '.xls' == os.path.splitext(each)[1]:
	# 		file.append(each)
	########################################
	return file

if __name__ == '__main__':
	get_file()

