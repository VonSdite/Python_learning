import time

# 显示 年-月-日 时:分:秒
# 2017-04-13 10:33:11
print(time.strftime('%F %X'))
# print(time.strftime('%F %T'))
print(time.strftime('%Y-%m-%d'))

# 显示 周几 月份 几日 时:分:秒 年
time.ctime(time.time())

# 显示小时和分钟  hh:mm
print(time.strftime('%R'))

# 标准日期串
# 月/日/年
print(time.strftime('%x'))