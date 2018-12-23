# 对爬取到的代理ip进行筛选，筛选出快速的代理

import pickle
import requests

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

with open('save.pkl', 'rb') as f:
    ip_list = pickle.load(f)

new_list = []
cnt = 0
for each in ip_list:
    cnt += 1
    try:
        res = requests.get(url=url, headers=headers, proxies={'http': each}, timeout=0.3) 
        new_list.append(each)
        print(cnt, 'pass')
    except:
        print(cnt, 'out')

# 用pickle保存下来
with open('save.pkl', 'wb') as f:
    pickle.dump(new_list, f)

print(len(new_list))
