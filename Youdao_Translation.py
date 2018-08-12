import urllib.request
import urllib.parse
import json
import time
import random
import hashlib

while(1):
    content = input('需要翻译的单词或句子:')


    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'



    data={}


    u = "fanyideskweb"
    d = content
    f = str(int(time.time()*1000) + random.randint(1,10))
    c = "ebSeFb%=XZ%T[KZ)c(sy!"
     
    sign = hashlib.md5((d + u + f + c).encode('utf-8')).hexdigest()

    data['i']= content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']= f
    data['sign']= sign
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_REALTIME'
    data['typoResult']='false'



    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url,data=data,method='POST')
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8") 
    target=json.loads(html)
    print("\n自动翻译的结果为：%s\n" %(target["translateResult"][0][0]["tgt"]))


