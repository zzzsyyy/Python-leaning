from random import *


answer = randint(1000,9999)
list = str(answer)
#list = '5111'


def cut(a):
    ls = []
    for i in a:
        ls.append(i)
    return ls

    
    
def compare(m,n):
    counter1=counter2=temp=temp2=0
    for i in range(len(m)):
        if i == 0:
            quchong = [m[i]]
            for j in range(len(n)):
                if m[i] == n[j]:
                    temp+=1
                    if i == j:
                        temp2 += 1
                        counter2 += 1
            if temp>1:
                counter1 += 1
                temp = 0
                temp2 = 0
        else:
            if m[i] in quchong:
                for j in range(len(n)):
                    if m[i] == n[j]:
                        temp+=1
                        if i == j:
                            temp2 += 1
                if temp==1 and temp2==1:
                    counter1 += 1
                    counter2 += 1
                    temp = 0
                    temp2 = 0
            else:
                for j in range(len(n)):
                    if m[i] == n[j]:
                        temp+=1
                        if i == j:
                            temp2 += 1
                            counter2 += 1
                if temp>1:
                    counter1 += 1
                    temp = 0
                    temp2 = 0
    return counter1,counter2

def iserror(a):
    if a.isdigit():
        if len(a)!= 4:
            print('请输入四位数')
    else:
        print('要输入一个四位数')
    return a.isdigit()==1 and len(a)==4
        
def main():
    print('按Enter键结束游戏！')
    num = input("键入你的猜想:")
    ls1 = cut(list)
    while num !='':
        
        attention = iserror(num)
        if attention != 1:
            num = input("键入你的猜想:")
            continue
        ls2 = cut(num)
        output = compare(ls1,ls2)
        if output[0]==4 and output[1] == 4:
            print("终于猜对了！！！")
            break
            
        print('有'+str(output[0])+'个数字正确，有'+str(output[1])+'个数字位置正确！')
        num = input("键入你的猜想:")
        
main()
