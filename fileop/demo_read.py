#-- coding:UTF-8 --
'''
Created on 2020��2��6��

@author: Administrator
'''
contentstr = "一行内容\n"
file = open('textfile.txt', 'w')
for i in range(1,10):
    file.write(contentstr)
file.close()
f = open('textfile.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()