#len()，，，返回列表长度
#str()，，，可以把整数转换为字符串然后才能进行写入文件，，，int()则反之
#open("文件路径",encoding='字符编码')，，，选择正确的字符编码才能正常读取文件
#file对象.readlines()在for的判断条件中出现之后不能在里面继续出现，需要创建一个对象在for外面接收readlines()的返回值，然后用这个创建的对象在for语句中重复使用
#字符串对象.find()或者字符串对象.index()返回的索引就是查找的字符串的第一个字符的位置
#python2和python3有点区别，导致了2有的方法在3没有或者不一样

import re

fileRead=open("read.txt", "r",encoding ='utf-16')
fileWrite=open("testWrite.txt","a")

##print(str(len(fileRead.readlines())))
for index in range(len(lines:=fileRead.readlines())):
    matchIt = re.search('(\d*)          未处理',lines[index])
    print('结果：',end='')
    if matchIt:
        #print(lines[index][lines[index].find('未处理')])
        print(flag:=int(matchIt.group(1))>300,end='')
        if flag:
            fileWrite.write(lines[index])
            print(' yes')
    print('。')

fileWrite.close()
fileRead.close()    
