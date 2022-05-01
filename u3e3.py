import re
class u3e3:
    def __init__(s,n):
        s.n=n 
        pattern=re.compile(r'00.{10}')
        r=re.findall(pattern,s.n)
        for i in r:
            i=i
        print(i)
n1=str(input())
e3=u3e3(n1)