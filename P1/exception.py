#异常处理
__author__ = 'hiCyoung'

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
#####异常捕获########
print("Step 1.....")
s=['1111"']
try :
    print("开始执行try....")
    fp = open("/ccccccccc","w")
    print("Step 1.5..........")
    print(s[1]) #数组越界
except IOError as e:  #捕获异常时，try-except块中产生异常的代码后面的代码不会执行，
                                # 如果异常没有被捕获，则整个后面代码都不会执行
    print(e)
except IndexError as e: #所有异常的父类是Exception
    print("[ERROR]:",e)
print("Step 2..........")


#####抛出异常（自定义）########
a = input("input age  between 10  and 20:")
try:
    if(10<=int(a)<=20):
        print("age is ",a)
    else :
        raise MyError('[ERROR]: age is  illegal')
except MyError as t:
    print(t)



