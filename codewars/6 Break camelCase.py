'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
'''

def solution(s):
    lis = list(s)
    counter = 0
    for i in range(len(s)):
        if 65<=ord(s[i])<=91:
            counter+=1
            print(i)
            lis.insert(i+counter-1," ")
    s1 = "".join(lis)
    return s1
