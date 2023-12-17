import urllib.request
import urllib.error

url = 'https://blog.csdn.net/sulixu/article/details/1198189491'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError as e:
    print('系统正在升级。。。' + str(e))
except urllib.error.URLError as e:
    print('我都说了 系统正在升级。。。' + str(e))
except Exception as e:
    print(type(e))
