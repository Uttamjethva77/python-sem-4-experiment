import mysql.connector

# try:
mydb=mysql.connector.connect(host="localhost",user="wincrics",password="k3ood0]]B33JYB",database="wincrics_wp246")
print(mydb)
# (str(e))
q=mydb.cursor()
q.execute("create table if not exists products(id int(2),name varchar(20),price int(5))")
mydb.commit()