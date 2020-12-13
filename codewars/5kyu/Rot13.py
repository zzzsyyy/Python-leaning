'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
'''

def rot13(message):
    s = ""
    for i in message:
        if 65<=ord(i)<=90:
            s += chr(65+(ord(i)-65+13)%26)
        elif 97<=ord(i)<=122:
            s += chr(97+(ord(i)-97+13)%26)
        else:
            s += i
    return s
