import random
N = eval(input('请输入模拟次数：'))
n = eval(input("请输入正确个数："))
def sub(m,n):
    a = ""
    for i in range(len(m)):
        if m[i] == n:
            continue
        else:
            a = a + m[i]
    return a
def xz():
    yd = ""
    xx = "ABCDEFG"
    for i in range(5):
        temp = random.choice(xx)
        xx = sub(xx,temp)
        yd = yd+temp
    return yd
def pd(yd):
    da = "ABCDE"
    c  = 0
    for i in range(5):
        if yd[i] == da[i]:
            c += 1 
    return c
def xh(N):
    s = 0
    for i in range(N):
        yd = xz()
        c  = pd(yd)
        if c == nm:
            s += 1
    return s
def main():
    s = xh(N)
    p = s/N
    print("对{:}个的概率是:{:.6f}".format(n,p))
    return 

main()
