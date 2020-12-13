'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(url):
    ls = url.split(".")
    for i in ls:
        if "//" in i and i[-2:] != "//" and i[-3:] != "www":
            domain = i.split("/")[-1]
            break
        elif "//" in i and i[-2:] != "//" and i[-3:] == "www":
            domain = ls[1]
            break
        elif "//" not in i and ls[0] != "www":
            domain = ls[0]
            break
        else:
            domain = ls[1]
            break
    return domain
