#--coding:GBK --
'''
Created on 2020��2��2��
@author: Administrator
''' 
import os 
import requests

print(os.getcwd())

r = requests.get("http://www.chinabbia.com")
print(r.text)