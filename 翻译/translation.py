import urllib.request as u
import urllib.parse as p
import json as j
import time as t

while True:
    print("-----------------------------------------------")
    context = ""
    while True:
        temp = str(input())
        if temp[-1] == '.':
            context += temp.replace('\n', ' ')
            break
        context += temp.replace('\n', ' ')
    
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    print(context)
    #head = {}
    #head['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"

    data = {}
    data['type'] = 'AUTO'
    data['i'] = context
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'

    data = p.urlencode(data).encode('utf-8')

    req = u.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = u.urlopen(req)

    html = j.loads(response.read().decode('utf-8'))

    print("翻译的结果是: " + html['translateResult'][0][0]['tgt'])
    print("-----------------------------------------------\n")



