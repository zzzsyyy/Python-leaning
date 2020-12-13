'''
The idea for this Kata came from 9gag today.here

You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet) wiki.

Like this:

Input:

If, you can read?

Output:

India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

Notes

The set of used punctuation is .!?.
Punctuation should be kept in your return string, but spaces should not.
Xray should not have a dash within.
Every word and punctuation mark should be seperated by a space ' '.
There should be no trailing whitespace
'''

def to_nato(words):
    str1=""
    dic = {'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo',\
    'F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliett',\
    'K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar',\
    'P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango',\
    'U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee','Z':'Zulu'}
    str = "".join(words.split())
    for i in str:
        if i.isalpha():
            str1+=dic[i.upper()]+" "
        else:
            str1+=i+" "
    return str1[:-1]
