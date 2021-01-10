#P
'''
Thisum = MaxSum = 0

def ifin():
    b = input()
    ls = [int(n) for n in b.split()]
    return ls

def Sum(ls):
    global Thisum,MaxSum
    for i in ls:
        Thisum += i
        if Thisum >=MaxSum:
           MaxSum = Thisum
        elif Thisum < 0:
            Thisum = 0
    return MaxSum
def main():
    ls = ifin()
    jg = Sum(ls)
    print(jg)
    
main()
'''


#N
'''def dele(ls,n):
    while "a" in ls:
        ls.remove("a")
    return ls

a = eval(input())
ls = list(range(a+1))
del ls[0]

while len(ls)!=1:
    if len(ls)%3==0:
        for i in range(len(ls)//3):
            ls[i*3+2]="a"
        ls = dele(ls,len(ls)//3)
    elif len(ls)%3==2:
        for i in range(len(ls)//3):
            ls[3*i+2]="a"
        ls[0]="a"
        ls.append(ls[0])
        ls = dele(ls,len(ls)//3)
    elif len(ls)%3==1:
        for i in range(len(ls)//3):
            ls[3*i+2]="a"
        ls[1]="a"
        ls.append(ls[0])
        ls.append(ls[1])
        ls = dele(ls,len(ls)//3)
        del ls[0]
print(int(ls[0]))'''

#M
'''a = input().split()
ls = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j and i!=k and j!=k:
                ls.append(str(a[i])+str(a[j])+str(a[k]))
max1 = min1 = eval(ls[0])
for i in range(6):
    if eval(ls[i])>max1:
        max1 = eval(ls[i])
    if eval(ls[i])<min1:
        min1 = eval(ls[i])
print(max1,min1)
'''

#J

a = input()
if a == "":
	print("0")
else:
	temp=""
	counter = counterx = 0
	for i in a :
		if i not in temp:
			temp+=i
			counter+=1
			if counterx<=counter:
				counterx = counter
		elif i in temp:
			counter = counter-temp.find(i)
			temp=temp[temp.find(i)+1:]
			temp+=i
	print(counterx)


#L
'''
ls=[]
ls1 = []
temp1=input()
k = ""
shuchu = ""
counter = 0
if temp1 == "":
	print("0")
else:
	while temp1!="":
		ls.append(temp1)
		temp1=input("")
	for i in ls:
		if i.isspace():
			ls1.append("0 ")
		elif i[-3:]=="ing":
			counter+=1
		elif i[-2:]=="ie":
			k = i[:-2]+"ying "
			ls1.append(k)
		elif i[-1]=="e":
			k = i[:-1]+"ing "
			ls1.append(k)
		else:
			k = i[:]+"ing "
			ls1.append(k)
	print(counter)
	for j in ls1:
		shuchu = shuchu+j
	print(shuchu[:-1])
'''
#I
'''
dic = {42:{"Blk Mgc":979,"CNY":879,"Third Eye Vision":1059,"TACO":1789},\
42.5:{"Blk Mgc":949,"CNY":869,"Third Eye Vision":1029,"TACO":1739},\
43:{"Blk Mgc":969,"CNY":879,"Third Eye Vision":989,"TACO":1719},\
44:{"Blk Mgc":869,"CNY":809,"Third Eye Vision":949,"TACO":1589}}

a = input()
b = eval(input())
print(dic[b][a])
'''

#C
'''ls = []
counter = sum = 0
a = eval(input())
if a == 0:
    print("0.000%")
else:
    for i in range(a):
        temp = eval(input())
        sum+=temp
        ls.append(temp)
    average=sum/a
    for i in ls:
        if i >average:
            counter+=1

    print("{:.3f}%".format(counter/a*100))
'''

#F
'''a = eval(input())
line = "1 "+"0 "*(a-2)+"0"
ls = line.split()
matrix=""
for i in range(a-1):
	matrix+=" ".join(ls)+"\n"
	ls[i]="0"
	ls[i+1]="1"


print(matrix+"0 "*(a-1)+"1")

'''

#A
'''
a = eval(input())
ls = []
for i in range(a):
	temp = input()
	ls.append(temp)
ls = reversed(ls)
for i in ls:
	print(i)
'''

#D
'''
ls = input().split()
ls1 = input()
ls1 = [int(i) for i in ls1.split()]
b = " ".join(ls[ls1[0]-1:ls1[1]])
print(b)
'''

#B
'''
a = eval(input())
ls = []
dic = {}
for i in range(a):
	temp = input()
	ls.append(temp)
	dic[i+1] = ls[i]
b = eval(input())
print(dic[b])
'''

#E
'''
ls = list(map(int,input().split()))
ls1 = []
ls2 = []
lsx = []
for i in ls:
	if i%2==0:
		ls2.append(i)
	else:
		ls1.append(i)
lsx = ls1+ls2
print(lsx)
'''
#G
'''
a = eval(input())
ls = []
sum1=sum2=0
for i in range(a):
	ls.append(list(map(int,input().split())))
for i in range(a):
	sum1 += ls[i][i]
	sum2 += ls[i][a-1-i]
print(sum1,sum2)
'''

#H
'''
a = eval(input())
dic = {}
for i in range(a):
	name = input()
	score = eval(input())
	dic[score]=name
ls = list(dic.keys())
x,y = max(ls),min(ls)
print(dic[y],y)
print(dic[x],x)
'''

#K
'''
a = eval(input())
b = a
string = ""
ls = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
for i in ls:
	while a%i==0:
		string += str(i)+"*"
		a = a/i
print("{} = {}".format(b,string[:-1]))
'''	


	
