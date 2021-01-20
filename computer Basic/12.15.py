#M
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
#K
'''
a=input()
c = 0
ls=a
if a[0]=="-":
    ls = a[::-1][:-1]
    c = 1
else:
    ls=ls[::-1]
while ls[0]=="0":
    ls=ls[1:]
if c==1:
    ls="-"+ls
print(ls)
'''
#I
'''
a = eval(input())
sum = 0
if a%2==0:
    s = a//2
    for i in range(s):
        sum += 1/(2*(i+1))
else:
    s = (a+1)//2
    for i in range(s):
        sum += 1/((2*i)+1)
print("{:.2f}".format(sum))
'''
#A
'''
def mm(m):
    if m>2:
        n = mm(m-1)+mm(m-2)
    else:
        n = 1
    return n
a = eval(input())
print(mm(a))
'''
#B
'''
def mm(m):
    if m>1:
        n = 2*mm(m-1)+1
    else:
        n = 1
    return n
a = eval(input())
print(mm(a))
'''
#C
'''
def ss(ls):
    s = len(ls)
    while s>1:
         i = 0
         while i <s-1:
            if ls[i]>ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
                i+=1
            else:
                i+=1
         s-=1
    return ls
a = list(map(int,input().split()))
print(ss(a))
'''
#D
'''
class student:
    def __init__(self,name,number,M,C,E):
        self.name=name
        self.number=number
        self.E=E
        self.C=C
        self.M=M
    def sum(self):
        sum = eval(self.M)+eval(self.C)+eval(self.E)
        return sum
a = []
for i in range(5):
    a.append(input())
print(student(a[0],a[1],a[2],a[3],a[4]).sum())
'''
#E
'''
class Bird:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def fun(self):
        print("aaa")
class Parrot(Bird):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.fun()
    def fun2(self):
        print('Hello!')
s = []
for i in range(4):
    s.append(input())
b = Bird(s[0],s[1])
c = Parrot(s[2],s[3])
c.fun()
c.fun2()
'''
#F
'''
class Cn:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def fprint(self):
        print("({}+{}j)".format(self.real,self.imag))
class BC(Cn):
    def __init__(self,real,imag):
        super().__init__(real,imag)
    def fprint(self):
        print("({}+{}j)".format(self.real,self.imag))
        print("{:.2f}".format((self.real**2+self.imag**2)**(1/2)))
a = eval(input())
b = eval(input())
Cn(a,b).fprint()
BC(a,b).fprint()
'''
#G
'''
class Student:
    n=0
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        Student.n+=1
a = input()
while a!="":
    ls = a.split()
    Student(ls[0],ls[1])
    a = input()
else:
    print(Student.n)
'''
#H
'''
def A(m):
    m["1"]="First"
    return m
dic = {}
for i in range(3):
    a = input().split()
    dic[a[0]]=a[1]
print(A(dic))
'''
#O
'''
a = eval(input())
ls1 = [1,1]
ls = [[1]]
ls2 = []
if a!=1:
    for i in range(a-2):
        for i in range(len(ls1)-1):
            ls2.append(ls1[i]+ls1[i+1])
        ls2.append(1)
        ls2.insert(0,1)
        ls.append(ls2)
        ls1 = ls2
        ls2 = []
    ls.insert(1,[1,1])
print(ls)
'''
#L
'''
ls = input().split()
set = set(ls)
c = 0
for i in set:
    if ls.count(i)>len(ls)//2:
        c = 1
        print(i)
if c==0:
    print(-1)
'''
#N
'''
c = input().split()
a = eval(c[0])
b = eval(c[1])
ls1 = []
sl = []
sl1 = []
for i in range(a):
    ls = input().split()
    ls1.append(ls)
for i in range(b):
    for j in range(a):
        sl.append(eval(ls1[j][i]))
    sl1.append(sl)
    sl = []
print(sl1)
'''
#J
'''
def fuc(arg1,*arg2,**arg3):
    print(arg1)
    print(arg2)
    print(arg3)
a = int(input())
b = eval(input())
c = eval(input())
d = eval(input())
e = input()
f = input()
fuc(a,b,c,d,name=e,age=f)

'''




















    
