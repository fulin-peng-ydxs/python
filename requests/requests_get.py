import requests

url = 'https://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data = {
    'wd': '北京'
}

# url  请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url, params=data, headers=headers)

content = response.text

print(content)

# 总结：
# （1）参数使用params传递
# （2）参数无需urlencode编码
# （3）不需要请求对象的定制
# （4）请求资源路径中的？可以加也可以不加
