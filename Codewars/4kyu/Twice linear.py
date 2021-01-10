'''
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency
'''

#每次取由两种计算得到的较小者
def dbl_linear(n):
    a = b = c = 0
    ls = [1]
    while a+b<n+c:
        x = 2*ls[a]+1
        y = 3*ls[b]+1
        if x<y:
            ls.append(x)
            a+=1
        elif y<x:
            ls.append(y)
            b+=1
        else:
            ls.append(x)
            a+=1
            b+=1
            c+=1        #c用来拓展边界，即当a=b时，a&b都变化了，而ls并未变
    return ls[-1]
