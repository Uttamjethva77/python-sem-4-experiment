import re
class u3e2:
    def __init__(s,w):
        s.w=w
        pattern=re.compile(r'{}'.format(s.w))
        a=re.findall(pattern,str1)
        print(len(a))
str1="A great chief is first a great technisian"
word=str(input())
e2=u3e2(word)

