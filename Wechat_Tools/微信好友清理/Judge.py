# coding=utf8
import itchat

CHATROOM_NAME = 'friend'  # 用于判断是否依旧是好友的 群名
CHATROOM = None

# 提示信息
HELP_MSG = u'''\
好友状态监测
* 发送名片将会返回好友状态
* 请确认名为%s的未使用的群聊
* 一定要是没使用的
* 这样对方才不会知道你创建了群聊
* 调用频率存在一定限制\
''' % CHATROOM_NAME

CHATROOM_MSG = u'''\
无法自动创建群聊，请手动创建
确保群聊名称为%s
请不要使用已经使用过的群聊
创建后请将群聊保存到通讯录\
''' % CHATROOM_NAME


# 获取群聊
# 其中CHATROOM是用于保存群聊, 提高程序的效率
# 执行过一次之后, get_chatroom()直接返回CHATROOM
def get_chatroom():
    global CHATROOM
    if CHATROOM is None:
        chatrooms = itchat.search_chatrooms(name=CHATROOM_NAME)
        # 搜索群聊是否已存在
        # 存在则返回
        # 不存在则创建
        if chatrooms:
            CHATROOM = chatrooms[0]
            return chatrooms[0]
        else:
        	# 创建群聊
            r = itchat.create_chatroom(
                itchat.get_friends()[1:3], topic=CHATROOM_NAME)
            if r['BaseResponse']['ErrMsg'] == u'请求成功':
                CHATROOM = {'UserName': r['ChatRoomName']}
            return CHATROOM
    else:
        return CHATROOM

# 判断好友状态
def get_friend_status(friend):
    global ownAccount

    # 推荐的名片是自己
    if friend['UserName'] == ownAccount:
        return u'检测到本人账号。'
    # 推荐的名片是你没加的人
    elif itchat.search_friends(userName=friend['UserName']) is None:
        return u'该用户不在你的好友列表中。'
    else:
    	# 获取群聊
        chatroom = get_chatroom()

        # 获取群聊失败，发送失败消息
        if chatroom is None:
            return CHATROOM_MSG
        # 将要判断的好友放入群聊中
        r = itchat.add_member_into_chatroom(chatroom['UserName'], [friend])
        # 如果成功拉入群聊
        # 表示对方还是好友
        if r['BaseResponse']['ErrMsg'] == u'请求成功':
            status = r['MemberList'][0]['MemberStatus']
            itchat.delete_member_from_chatroom(chatroom['UserName'], [friend])
            return {3: u'该好友已经将你加入黑名单。',
                    4: u'该好友已经将你删除。', }.get(status,
                                            u'该好友仍旧与你是好友关系。')
        else:
            return u'无法获取好友状态，预计已经达到接口调用限制。'


@itchat.msg_register(itchat.content.CARD)
def get_friend(msg):
    if msg['ToUserName'] != 'filehelper':
        return
    friendStatus = get_friend_status(msg['RecommendInfo'])
    itchat.send(friendStatus, 'filehelper')

itchat.auto_login(hotReload=True) 		# 登陆

ownAccount = itchat.get_friends(update=True)[0]['UserName']  # 本人账号名

itchat.send(HELP_MSG, 'filehelper')  # 发送操作消息给自己

itchat.run()
