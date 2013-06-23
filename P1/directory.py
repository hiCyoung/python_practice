#文件与目录模块
__author__ = 'hiCyoung'
import  os

#具体参照API
gn = os.walk("D:"+os.sep+"appLinks");
for i in gn:
    print(i)
