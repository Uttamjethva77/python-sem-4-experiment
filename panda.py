import pandas as pd

dict ={'names':["ABC","XYZ","PQR"],'marks':[50,90,30]}

df=pd.DataFrame(dict)

data=pd.read_csv('stud.csv')
print(data)
print(data.info())