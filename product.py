print ("db created")
conn1.execute('drop table if exists product')
conn1.commit()
conn1.execute('''create table if not exists student(
id int not null,
product name text,
cost text
) ''')
print('table created')
    

print ("""press 1 to add record
press 2 display record
press 3 update record
press 4 delet record""")

a=int(input("enter your choice"))