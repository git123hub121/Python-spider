import urllib.request
import urllib.parse
#   response   响应
#   urlopen后面还有许多可选项，如data,timeout,cafile等等
data = bytes(urllib.parse.urlencode({'word': 'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())

#   结果
#   "form": {\n    "word": "hello"\n  } 以表单形式