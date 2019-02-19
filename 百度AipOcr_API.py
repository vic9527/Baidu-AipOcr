# coding:utf-8

import urllib, urllib.request, sys, base64
import ssl, win32ui

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=rzz6wNkWGoqnchpZ4y91HAvn&client_secret=6iknf0e5PHXb82qcSKkCvCAPohgrwf8F'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
#if (content):
#    print(content)
    
def convert(data):
    if isinstance(data, bytes):  return data.decode('ascii')
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    return data

content_str = convert(content)
content_dict = eval(content_str)

    
access_token = content_dict['access_token']
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token
# 二进制方式打开图文件
dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
dlg.SetOFNInitialDir('C:') # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName() # 获取选择的文件名称
filestring = filename.replace("\\","/") # 替换/为\
f = open(filestring, 'rb')
#f = open(r'文字.jpg', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
params = urllib.parse.urlencode(params).encode(encoding='UTF-8')
request = urllib.request.Request(url, params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
PicWord = response.read().decode()
#if (isinstance(PicWord, dict)):
    #print(PicWord)
#else:
PicWord = eval(PicWord)
    #print("转换字典后输出：")
    #print(PicWord)

for i in PicWord['words_result']:
    print(i['words'])

