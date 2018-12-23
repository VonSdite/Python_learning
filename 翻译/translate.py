import requests
import json as j

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

data = {
    "from": "AUTO",
    "to": "AUTO",
    "client": "fanyideskweb",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_ENTER",
    "typoResult": "true"
}

s = requests.Session()

print("开始翻译: ")
while True:
    print("-----------------------------------------------")
    context = ""
    while True:
        temp = str(input())
        try:
            if temp[-1] == '.':
                context += temp + ' '
                break
            context += temp + ' '
        except:
            context += temp + ' '
            break

    data['i'] = context
    res = s.post(url=url, headers=headers, data=data)

    html = j.loads(res.text)
    context = ""
    for result in html['translateResult'][0]:
        context += result["tgt"]
    print("翻译的结果: ")
    print(context)
    print("-----------------------------------------------\n")
