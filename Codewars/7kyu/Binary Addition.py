'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.
'''
def add_binary(a,b):
    ls = ''
    c = a+b
    while c != 1:
        s = c%2
        ls += str(int(s))
        c = (c-s)//2
    ls += str(int(c))
    ls = ls[::-1] 
    return ls
