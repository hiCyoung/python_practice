####字典:键值对（Key-Value）

__author__ = 'hiCyoung'

d = {}
print(type(d))
d["a"]=1   #添加元素
d['b']=2
print(d)
d['c']=3
d['d']=2
print(d)  #字典是无序的！！！！
print(d['a'])  #访问元素

for k in d:  #遍历
    print(k,d[k])

del d['a']  #删除元素
print(d.pop('b')) #删除元素并且返回对应Value
print(d)

##字典常用方法
print(d.keys())
print(d.values())
print(d.items())  #转换为元组

d1={"ff":(1,2),"bb":(3,4),"cc":(5,6),"rs":(7,8)}
print(d1)
t=sorted(d1.items()) #对字典排序
print(t)