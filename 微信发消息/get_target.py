import glob
import pyexcel

# 从已有的学习心得中获取已提交的名单
def get_submitted():
    path = 'C:/Users/Sdite/Desktop/学习心得'     # 获取名单的路径
    f1 = glob.glob(path + '/*.docx')             # 均为文件的后缀格式，具体情况改变
    f2 = glob.glob(path + '/*.doc')
    f3 = glob.glob(path + '/*.odt')
    f4 = glob.glob(path + '/*.rtf')
    f1 = [name.split('\\')[1][9:].split('.')[0] for name in f1] #第二个split是为了筛出名字
    f2 = [name.split('\\')[1][9:].split('.')[0] for name in f2]
    f3 = [name.split('\\')[1][9:].split('.')[0] for name in f3]
    f4 = [name.split('\\')[1][9:].split('.')[0] for name in f4]
    file = f1 + f2 + f3 + f4
    return file


def get_members():
    sheet = pyexcel.get_sheet(
        file_name="C://Users//Sdite//Desktop//学习心得//1.xls")
    members = sheet.column[0]  #获取excel中的一列名单
    return members


def get_rest():
    submit_person = get_submitted()
    members = get_members()
    rest = list()
    #做差集
    for person in members:
        if person not in submit_person:
            rest.append(person)
    return rest


if __name__ == '__main__':
    rest = get_rest()
    print(rest)
