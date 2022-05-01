import re
class u3e1:
    def __init__(s,w):
        s.w=w
        pattern=re.compile(r'co')
        if re.search(pattern,s.w):
            print("match")
        else:
            print("not")
word=str(input())
e1=u3e1(word)

