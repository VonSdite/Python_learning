import pyexcel

# 处理为个人空课表
def deal(sheet, name):
    name = name.split('.')[0].split('\\')[-1]
    for row in range(3, 8):
        for col in range(1, 14):
            # 跳过午休时间段

            if col in [5, 6]:
                sheet[row, col] = ''
                continue

            if '' != sheet[row, col]:
                sheet[row, col] = ''
            else:
                sheet[row, col] = name + ' '
    return sheet

# 计算每个表格人数
def calc(sheet):
    for row in range(3, 8):
        for col in range(1, 14):
            # 跳过午休时间段

            if col in [5, 6]:
                sheet[row, col] = ''
                continue

            if '' != sheet[row, col]:
                sheet[row, col] += '共' + \
                    str(len(sheet[row, col].split(' ')) - 1) + '人'
    return sheet


# 合并空课表
def merge(final, sheet):
    for row in range(3, 8):
        for col in range(1, 14):
            # print("(%d,%d) %s %s", row, col, final[row, col], sheet[row, col])
            final[row, col] += sheet[row, col]
    return final


def init_sheet(name):
    sheet = pyexcel.get_sheet(file_name=name)
    sheet[0, 0] = ''
    for row in range(3, 8):
        for col in range(1, 14):
            sheet[row, col] = ''
    return sheet
