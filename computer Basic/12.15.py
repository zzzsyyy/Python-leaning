'''
a = eval(input())
while a!=1:
    if a%2==0:
        a/=2
        counter+=1
    else:
        a=3*a+1
        counter+=1
print(counter)

'''

a=input()
if a[0]=="-":
	ls = a[:-1:-1]
print
