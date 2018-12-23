import os
import random as rn

class Question:
    def __init__(self,word, answer, source):
        self.word = word
        self.answer = answer
        self.source = source

    def check(self, answer):
        boolean = answer.upper().replace(' ', '') == self.answer.upper().split('；')[0].replace(' ', '')
        if boolean:
            print('答对啦')
        else:
            print('答错了')
        print('答案：%s考题来源：%s' % (self.answer.replace(' ', ''), self.source.replace(' ', '')))
        return boolean
def splitques(content):
    return content.split('一、单项选择题')[-1].split('二、多项选择题')
    
def splitanswer(question):
    spques = {}
    i = 1
    while question:
        question = question.split('%d、' % i,1)[-1]
        temp = question.split('%d、' % (i+1), 1)
        temp1 = temp
        question =  '%d、' % (i+1) + temp[-1] 
        temp = temp[0].partition('答案：')
         
        spques[i] = [temp[0]]
        temp = temp[-1].split('考题来源：')
        spques[i].extend(temp)
        if len(temp1) == 1:
            break
        i += 1
    return spques

while 1:
    boolean = input('是否进入自测系统：Y/N').upper()
    if boolean == 'Y':
        print('欢迎进入自测系统')    
        while 1:
            file = input('输入题库路径：')
            if os.path.exists(file):
                break
            else:
                print('文件不存在')

        while 1:
            try:
                count1 = int(input('输入单选题目数量：'))
            except ValueError:
                print('输入的不是正整数：')
            else:
                break

        while 1:
            try:
                count2 = int(input('输入多选题目数量：'))
            except ValueError:
                print('输入的不是正整数：')
            else:
                break
            
        f = open(file,'r')
        content = f.read()
        f.close()
        ques = splitques(content)

        part1 = splitanswer(ques[0])
        len1 = len(part1.keys())
        onechoice = []
        multichoice = []
        
        for i in range(len1):
            question = Question(part1[i+1][0], part1[i+1][1], part1[i+1][2])
            onechoice.append(question)

        part2 = splitanswer(ques[1])
        len2 = len(part2.keys())
        for i in range(len2):
            question = Question(part2[i+1][0], part2[i+1][1], part2[i+1][2])
            multichoice.append(question)   
        while 1:
            boolean = input('是否开始考试或退出系统：Y/N').upper()
            if boolean == 'Y':
                num1 = []
                num2 = []
                right = 0
                print('考试开始：')
                print('=============================================================================== ')

                print('以下是单选题：')
                onecho = onechoice.copy()
                for i in range(count1):
                    num = rn.randint(0,len1-1-i)
                    temp = onecho.pop(num)
                    print('%d、' % (i+1)+temp.word)
                    if temp.check(input('输入回答:')):
                        right += 1
                print('=============================================================================== ')
                print('以下是多选题：')
                mulcho = multichoice.copy()
                for i in range(count2):
                    num = rn.randint(0,len2-1-i)
                    temp = mulcho.pop(num)
                    print('%d、' % (i+1)+temp.word)
                    if temp.check(input('输入回答:')):
                        right += 1
                print('考试结束')
                print('=============================================================================== ')
                print('正确率是{0:.2f}%'.format(right/(count1+count2)*100))
                boolean = input('是否重考：Y/N').upper()
                if boolean != 'Y':
                    print('系统已退出，欢迎再次使用')
                    break
            else:
                print('系统已退出，欢迎再次使用')
                break
            

