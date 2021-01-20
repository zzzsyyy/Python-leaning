from random import *

is_error = 1

#将得到的输入拆分并装入列表
def cut(a):
    ls = []
    ls.extend(a)
    return ls

#比较两个数，返回答案中有你的几个数
#m = answer   n = your_answer
def compare_1(m,n):
    count_1 = 0
    set_answer = set(m)
    ls_temp = []
    for i in n:
        if i in set_answer and i not in ls_temp:
            count_1 += 1
            ls_temp.append(i)
    return count_1

#比较两个数，返回位置正确的个数
def compare_2(m,n):
    
    count_2 = 0
    for i in range(4):
        if m[i] == n[i]:
            count_2 += 1
    return count_2

#处理输入不规范的情况
def iserror(a):
    if a.isdigit():
        if len(a)!= 4:
            print('请输入四位数')#如果不是四位
    else:
        print('要输入一个四位数')#如果不是数字
    return a.isdigit()==1 and len(a)==4#正常返回 1 ，否则返回 0


#主函数        
def main():
    count_2 = count_1 = count = 0
    answer = list(str(randint(1000,9999)))
    while count_2 !=  4:
        your_input = input("请键入你的猜想：")
        is_error = iserror(your_input)
        while is_error == 0:
            break
        else:
            your_answer = cut(your_input)
            count += 1
            count_1 = compare_1(answer,your_answer)
            count_2 = compare_2(answer,your_answer)
            if count_2 != 4:
                print("你说中了{}个数字，有{}个数字位置正确！".format(count_1,count_2))
            else:
                print("终于猜对了！！！")
                print("你用了{}次！".format(count))


def naother():
    main()
    tem = input("按y重新游戏，按Enter退出")
    while tem in ["y","Y"]:
        main()
        tem = input("按y重新游戏，按Enter退出")
    else:
        exit()


naother()
