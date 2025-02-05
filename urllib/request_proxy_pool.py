import urllib.request
import random

# 代理池
proxies_pool = [
    {'http': '118.24.219.151:16817'},
    {'http': '118.24.219.151:16817'},
]
# 随机从代理池选取某个代理ip
proxies = random.choice(proxies_pool)
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('daily.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
