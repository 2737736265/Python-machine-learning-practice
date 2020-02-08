#-- coding:UTF-8 --
'''
Created on 2020��2��4��

@author: Administrator
'''
#猜数字，猜对为止
num = 88
guess_flag = False
i = 0
while guess_flag == False:
    i+=1
    print("第{0}次猜测ʼ\n".format(i))
    while True:
        try:
            userGuess = int(input("输入你猜的数字:"))
            break
        except ValueError:
            print("输入的不是数字，请重新输入\n")
    if userGuess == num:
        print("猜对了") 
        guess_flag = True 
    elif userGuess > num:
        print("猜大了")
    else:
        print("猜小了")
print("游戏结束")