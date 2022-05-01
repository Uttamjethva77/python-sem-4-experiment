import re
class u3e4:
    def __init__(s,n):
        s.n=n 
        pattern=re.compile(r'^h+\w+o$')
        m=re.findall(pattern,s.n)
        if len(m)>0:
            print("match")
        else:
            print("not match")
n1=str(input())
e4=u3e4(n1)
