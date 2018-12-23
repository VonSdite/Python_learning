import itchat
import time

CHATROOM_NAME = u'CleanRoom'  # 用于判断是否依旧是好友的 群名

# 提示信息
MESSAGE = u'''\
系统启动
* 开始检测非好友关系的用户\
'''

FAILED = u'''\
无法自动创建群聊，请手动创建
确保群聊名称为%s
请不要使用已经使用过的群聊
创建后请将群聊保存到通讯录\
''' % CHATROOM_NAME
SUCCESS = u'''\
运行结束
请手动删除群聊\
'''

class Wechat(object):
    """docstring for Wechat"""

    def __init__(self):
        super(Wechat, self).__init__()

    # 获取好友列表
    def get_friends(self):
        friends = itchat.get_friends()
        return friends

    # 获取群聊
    def get_chatroom(self):
        chatrooms = itchat.search_chatrooms(name=CHATROOM_NAME)
        # 搜索群聊是否已存在
        # 存在则返回
        # 不存在则创建
        if chatrooms:
            return chatrooms[0]
        else:
            friends = itchat.get_friends()[1:3]
            # 创建群聊
            r = itchat.create_chatroom(
                friends, topic=CHATROOM_NAME)
            itchat.delete_member_from_chatroom(r['ChatRoomName'], [friends[0], friends[1]])
            if r['BaseResponse']['ErrMsg'] == u'请求成功':
                return {'UserName': r['ChatRoomName']}
            else:
                return None

    def judge(self):
        # 获取该用户账户名
        ownAccount = itchat.get_friends(update=True)[0]['UserName']
        # 获取好友列表
        friends_list = self.get_friends()
        # 获取群聊
        chatroom = self.get_chatroom()

        # 获取群聊失败，发送失败信息
        if chatroom is None:
            return FAILED
        else:
            for person in friends_list:
                if ownAccount == person['UserName']:
                    continue
                r = itchat.add_member_into_chatroom(
                    chatroom['UserName'], [person])
                # 如果成功拉入群聊
                # 表示对方还是好友
                if r['BaseResponse']['ErrMsg'] == u'请求成功':
                    # 获取拉入状态
                    # 3:为加入黑名单了
                    # 4:为被删除了
                    # 其他则仍是好友
                    status = r['MemberList'][0]['MemberStatus']
                    time.sleep(3)
                    itchat.delete_member_from_chatroom(
                        chatroom['UserName'], [person])
                    itchat.send(
                    {3: u'该好友%s已经将你加入黑名单。' % (person['RemarkName'] or person['NickName']),
                     4: u'该好友%s已经将你删除。' % (person['RemarkName'] or person['NickName'])}.get(status,
                     u'该好友%s仍旧与你是好友关系。' % (person['RemarkName'] or person['NickName'])),
                        'filehelper')
                    time.sleep(5)
            return SUCCESS

    def login(self):
        # 登陆
        itchat.auto_login(hotReload=False)
        # 发送提示消息
        itchat.send(MESSAGE, 'filehelper')

    def logout(self):
        itchat.logout()

    def run(self):
        itchat.send(self.judge(), 'filehelper')

if __name__ == '__main__':
    User = Wechat()
    User.login()
    User.run()
    User.logout()
