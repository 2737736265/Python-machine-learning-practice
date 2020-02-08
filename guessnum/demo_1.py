#-- coding:UTF-8 --
'''
Created on 2020��2��4��

@author: Administrator
'''
#猜数字，只允许猜一次
num = 88
print("开始猜测ʼ\n")
userGuess = int(input("输入你猜的数字:"))
if userGuess == num:
    print("猜对了")  
elif userGuess > num:
    print("猜大了")
else:
    print("猜小了")