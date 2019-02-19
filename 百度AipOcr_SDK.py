#!/usr/bin/python 
# -*- coding: utf-8 -*-

from aip import AipOcr
import win32ui


""" 你的 APPID AK SK """
APP_ID = '11271246'
API_KEY = 'rzz6wNkWGoqnchpZ4y91HAvn'
SECRET_KEY = '6iknf0e5PHXb82qcSKkCvCAPohgrwf8F'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
dlg.SetOFNInitialDir('C:') # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName() # 获取选择的文件名称
filestring = filename.replace("\\","/") # 替换/为\

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(filestring)

""" 调用通用文字识别, 图片参数为本地图片 """
result1 = client.basicGeneral(image);
result2 = client.basicAccurate(image);

print("通用版：\n")
for i in result1['words_result']:
    print(i['words'])
print("\n")
print("\n")
print("\n")
print("高精度版：\n")
for i in result2['words_result']:
    print(i['words'])