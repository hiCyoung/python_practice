#文件与目录模块
__author__ = 'hiCyoung'


#open具体用法参照help文档
fp =open("../README","r")
strs=fp.readlines()
for str in strs:
    print(str)
fp.close();

#写文件，没有文件新建，有的话就内容覆盖
fp = open("../NEWFILE","w")
fp.write("Hello,wolrd\r")
fp.writelines(strs)
fp.close();

