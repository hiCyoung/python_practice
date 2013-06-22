#函数
__author__ = 'hiCyoung'
def f(x,y):
    return x+y

def sayHello():
    print("Hello,Cyoung")
#           没有返回值的函数默认会加上 return None

#给参数设置默认值
def defaultValue(x,y=3):  #不能是(x=3,y)
         print("x=",x," y=",y)
         return x**2+y**3
print(f(1,2))
sayHello()
print(3**3)
print(defaultValue(2))
print(defaultValue(2,1))
print(defaultValue(y=2,x=3)) #关键字，破除了函数参数定义顺序的限制
print(defaultValue(x=2,y=3))
###递归函数##
def jc(n):
    if n ==1:
        return 1
    else:
        return n*jc(n-1)
print(jc(5))