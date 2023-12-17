import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://www.baidu.com/s?wd=周杰伦
# http/https    www.baidu.com   80/443     s      wd = 周杰伦     #
#    协议             主机        端口号     路径     参数           锚点


# 因为urlopen方法中不能存储字典 所以headers不能传递进去
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(headers=headers, url=url)

# 传递请求对象
response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)
