__author__ = 'hiCyoung'
#while流程控制 1
listL = []
name=input('input name: ')
while True:
    if len(name)==0:
        break
    listL.append(name)
    name=input("input name: ")
print(listL)
print(len(listL))

#while流程控制 2
listL2 = []
name=input('input name2: ')
while name:
    listL2.append(name)
    name=input("input name2: ")
print(listL2)
print(len(listL2))

###for循环
for i in range(1,5):
    for j in range(2,5):
        print(j)
        if i==j:
            break
