__author__ = 'hiCyoung'
digit = []
sum = 0
max = 0
min = 0
while True:
    d = input("input a number: ")
    if d=="":
        break
    k = int(d)
    digit.append(d)
    if len(digit)==1:
        min = k
    if k>max:
        max=k
    if k<min:
        min=k
    sum+=k

print("count=",len(digit),",sum=",sum,",max=",max,"min=",min)
