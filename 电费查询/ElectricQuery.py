# -*- coding: utf-8 -*-
# @Author   : Sdite
# @DateTime : 2017-06-06 14:03:59

import requests
import time
import sys
import re
import os


class PowerQuery(object):
    """docstring for PowerQuery"""

    def __init__(self, DormNum):
        self.LoginUrl = "http://202.116.25.12/Login.aspx"   # 登陆的url
        self.url = "http://202.116.25.12/default.aspx"      # default的url
        self.DormNum = DormNum                      # 宿舍号
        self.cookie = self.GetCookie()              # 获取页面cookie

        # 获取 VIEWSTATE 和 EVENTVALIDATION 以及宿舍对应的编号self.num
        info = self.GetViewstateAndEventvalidation()
        self.viewstate = info['VIEWSTATE']
        self.eventvalidation = info['EVENTVALIDATION']

    def Query(self):
        print("宿舍号: %s" % self.DormNum)
        self.RestPower()
        self.UsedHistroy()

    # 获取页面cookie
    def GetCookie(self):
        # Returns:
        # 返回登陆cookie
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "302",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "http://202.116.25.12/Login.aspx",
            "Host": "202.116.25.12",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Upgrade-Insecure-Requests": "1",
        }
        data = {
            "__LASTFOCUS": "",
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": "/wEPDwULLTE5ODQ5MTY3NDlkZM4DISokA1JscbtlCdiUVQMwykIc",
            "__EVENTVALIDATION": "/wEWBQLz+M6SBQK4tY3uAgLEhISACwKd+7q4BwKiwImNC7oxDnFDxrZR6l5WlUJDrpGZXrmN",
            "__VIEWSTATEGENERATOR": "C2EE9ABB",
            "txtname": str(self.DormNum),
            "hidtime": time.strftime('%F %X'),
            "txtpwd": "",
            "ctl01": "",
        }
        s = requests.Session()
        r = s.post(url=self.LoginUrl, headers=headers, data=data)
        cookie = r.headers.get("set-cookie")
        cookie = cookie.split(";")
        cookie = cookie[0] + ";" + cookie[2][8:]
        return cookie

    def GetViewstateAndEventvalidation(self):
        # Returns:
        # 返回Info是一个字典，包含VIEWSTATE和EVENTVALIDATION
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "cookie": self.cookie,
            "Connection": "keep-alive"
        }

        r = requests.get(url=self.url, headers=headers)
        content = r.text
        regular = {
            'viewstate': re.compile(r'id="__VIEWSTATE" value="(.+)" />'),
            'eventvalidation': re.compile(r'id="__EVENTVALIDATION" value="(.+)" />')
        }
        Info = dict()
        Info['VIEWSTATE'] = regular['viewstate'].findall(content)[0]
        Info['EVENTVALIDATION'] = regular['eventvalidation'].findall(content)[
            0]
        part = re.compile(r'"(\[电表\]\|.+?)"')
        self.num = str(part.findall(content)[0])
        return Info

    def RestPower(self):
        # Returns:
        # 输出剩余电量
        data = {
            "__EVENTTARGET": "RegionPanel1$Region2$GroupPanel1$ContentPanel1$DDL_监控项目",
            "__VIEWSTATE": self.viewstate,
            "__VIEWSTATEGENERATOR": "CA0B0334",
            "__EVENTVALIDATION": self.eventvalidation,
            "PandValue": "10",
            "hidpageCurrentSize": "1",
            "hidpageSum": "1",
            "hidpageCurrentSize2": "1",
            "hidpageSum2": "4",
            "hidpageCurrentSize3": "1",
            "hidpageSum3": "25",
            # "RegionPanel1$Region3$ContentPanel3$txtstarOld": "2017-5-2",
            # "RegionPanel1$Region3$ContentPanel3$txtstar": "2017-6-2",
            "__12_value": self.num,
            "RegionPanel1$Region3$ContentPanel3$tb_ammeterNumb": self.num[0:4] + self.num[5:],
            "__41_value": "00900200",
            "RegionPanel1$Region1$GroupPanel2$Grid3$Toolbar2$pagesize3": "1",
            "RegionPanel1$Region1$GroupPanel2$Grid2$Toolbar3$pagesize2": "1",
            "RegionPanel1$Region1$GroupPanel2$Grid1$Toolbar1$pagesize": "1",
            "__box_page_state_changed": "false",
            "__12_last_value": self.num,
            "__41_last_value": "00000000",
            "__box_ajax_mark": "true",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "cookie": self.cookie
        }
        r = requests.Session().post(url=self.url, data=data, headers=headers)
        res = r.text
        part = re.compile(r'box.__27.setValue\("(.+?)"\)')
        # print(part.findall(res))
        res = part.findall(res)[0]
        print("当前剩余电量: %s度" % res)

    def UsedHistroy(self):
        # Returns:
        # 直接输出电量使用记录
        data = {
            "__EVENTTARGET": "RegionPanel1$Region1$GroupPanel2$Grid2$Toolbar3$pagesize2",
            "__VIEWSTATE": self.viewstate,
            "__VIEWSTATEGENERATOR": "CA0B0334",
            "__EVENTVALIDATION": self.eventvalidation,
            "PandValue": "10",
            "hidpageCurrentSize": "1",
            "hidpageSum": "1",
            "hidpageCurrentSize2": "1",
            "hidpageSum2": "4",
            "hidpageCurrentSize3": "1",
            "hidpageSum3": "25",
            # "RegionPanel1$Region3$ContentPanel3$txtstarOld": "2017-5-2",
            # "RegionPanel1$Region3$ContentPanel3$txtstar": "2017-6-2",
            "__12_value": self.num,
            "RegionPanel1$Region3$ContentPanel3$tb_ammeterNumb": "[电表]000001213787",
            "__41_value": "00000000",
            "RegionPanel1$Region1$GroupPanel2$Grid3$Toolbar2$pagesize3": "1",
            "RegionPanel1$Region1$GroupPanel2$Grid2$Toolbar3$pagesize2": "4",
            "RegionPanel1$Region1$GroupPanel2$Grid1$Toolbar1$pagesize": "1",
            "__box_page_state_changed": "true",
            "__12_last_value": self.num,
            "__41_last_value": "00000000",
            "__box_ajax_mark": "true",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KUsedHistroy, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "cookie": self.cookie,
            "X-Requested-With": "XMLHttpRequest"
        }

        r = requests.Session().post(url=self.url, data=data, headers=headers)
        res = r.text.split('[')
        part = re.compile(r'"(.+?)"')

        # 将列表反向，是为了让日期降序输出
        res.reverse()
        print('********************************')
        print("电量使用历史记录: \n")
        print("   日期      用电量   用电金额")
        for x in res[1:-2]:
            x = part.findall(x)
            print("%s   %5s度 %7s元" % (x[0], x[1], x[2]))

if __name__ == '__main__':
    try:
        DormNum = sys.argv[1]
    except:
        DormNum = '3607'
    PowerQuery(DormNum=DormNum).Query()

    # 下列是为了方便查询多个宿舍所使用的代码
    # while True:
    #     try:
    #         dormNum = int(input("请输入宿舍号: "))
    #         os.system("cls")
    #         dorm = PowerQuery(DormNum=dormNum)
    #         dorm.Query()
    #         del dorm                    # 释放对象
    #     except AttributeError:
    #         print("输入的宿舍号有误！请重新输入")
    #     except EOFError:
    #         exit(0)
