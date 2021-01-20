MaxSum = -1e100
Thisum = R = L = cache = 0
def ifin():
    b = input()
    a = input()
    ls = [int(n) for n in a.split()]
    return ls
def Sum(ls):
    global Thisum,MaxSum,L,R,cache
    for i in range(len(ls)):
        Thisum += ls[i]
        if Thisum > MaxSum:
            MaxSum = Thisum
            L = cache
            R = i
        if Thisum < 0:
                Thisum = 0
                cache = i+1
    if MaxSum < 0:
            MaxSum = 0
            L = 0
            R = -1
    return MaxSum,L,R
def main():
    ls = ifin()
    jg = Sum(ls)
    print('{} {} {}'.format(MaxSum,ls[L],ls[R]))
main()
