import urllib.request

url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 代理地址：请求发送给代理服务器，由代理服务器执行真实url请求并将结果返回
# 例如快代理平台
proxies = {
    'http': '118.24.219.151:16817'
}
# 代理处理器
handler = urllib.request.ProxyHandler(proxies=proxies)
# handler  build_opener  open ：
opener = urllib.request.build_opener(handler)
response = opener.open(request)
# 获取响应的信息
content = response.read().decode('utf-8')
# 保存
with open('daily.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
