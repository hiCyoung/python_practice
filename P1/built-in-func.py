#内置函数
__author__ = 'hiCyoung'

#绝对值
print(abs(1+2j))

def a():
    print("aa")

def b():
    return 3
#判断一个函数能否被调用
print(callable(a()))

#返回商、余
print(divmod(10,3))
print(divmod(-10,3))

#类型判断
print(isinstance(12,int))
print(isinstance(12,str))
print(isinstance(12,(str,int)))  #判断12的类型是不是在元组内
print(isinstance(a(),str))
print(isinstance(b(),int))

#获取长度
print(len({"aaa":1,"bbb":2}))

#幂函数
print(pow(2,4))  #等同于2**4

#返回某个范围内的连续证书列表
print(list(range(1,10,2)))
print(range(1,10,2)[1])

#四舍五入（后一参数表示保留几位小数）
print(round(3.1415926,3))

#类型转换
print(chr(97))
print(int(12.3))
print(list("hello"))
print(tuple("hello"))