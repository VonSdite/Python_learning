import os
import glob
 
def get_file():
	path = os.getcwd()				# 获取当前路径

	file = list()

	# all_file = os.listdir(path)
	# print(all_file)
	# 即可获取当前路径下所有文件名

	# 获取当前路径下所有.xls文件名
	# 当然，用glob会更简单(是绝对路径的)
	# file = glob.glob(path+'/*.xls')
	for each in os.listdir(path):
		# os.path.splitext作用是将文件名分成文件名和扩展名
		if '.xls' == os.path.splitext(each)[1]:
			file.append(each)


	return file

if __name__ == '__main__':
	get_file()

