import re;
test ='''

123456789
abcdefghigh
ABVDEFGHI
Mr shahid
Mr.meet
Ms gautami
Ms. chaturi
!@#23536$%^^&*(())
https://www.uttam.rku.com
http://www.uttam.rku.com
https://uttam.rku.net
http://uttam.rku.com
uttam_jethva@gmail.net
uttam.jethva.@gmail.com
_-*/-
'''
# patten=re.compile(r'\d')
# patten=re.compile(r'https?://(www\.)?(\w)+.(\w)+.(com|in|net)')

f=open("sha.txt", "r")
content = f.read()

patten=re.compile(r'[a-zA-Z0-9-_.]+@(\w)+.(com|net|in)')

#pattern=re.compile(r'\d{10}')

#pattern=re.compile(r'https?://(www\.)?[a-zA-Z]+[.](com|net|gov|org|mil)')

#pattern=re.compile(r'Mrs?[.]\s?[a-zA-Z]+')

#pattern=re.compile(r'[\+91]?\d{10}')

#pattern=re.compile(r'[a-zA-Z0-9]+[@](gmail|yahoo|hotmail)[.](com|net|gov|org|mil)')

pattern=re.compile(r'[98]+[0-9]{2}-[0-9]{3}-[0-9]{3}')

datas=pattern.finditer(content)
for data in datas:
    print(data)