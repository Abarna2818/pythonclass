#
'''show Connection object'''
""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire")
print(connection) """
#
# '''Create database'''
""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("create database pysql") """
#
#
'''show all databases with in root user'''
""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
   print(x) """
#
#
#
# '''Create table '''
""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="pysql")
cursor=connection.cursor()
cursor.execute("create table table1 (name varchar(255),age int)")
cursor.execute("show tables")
print("Number of tables in database :")
for x in cursor:
     print("\t",x) """



""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="pysql")
cursor=connection.cursor()
cursor.execute("create table table2 (id int auto_increment primary key not null,name varchar(255))")
cursor.execute("select * from table2")
print("Number of tables in database :")
for x in cursor:
    print("\t",x) """


""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="pysql")
cursor=connection.cursor()
s="insert into table2(name) values(%s)"
t=("calvin")
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid) """

""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="pysql")
cursor=connection.cursor()
s="insert into table2(name) values(%s)"
t=[("java"),("c++")]
cursor.executemany(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid) """


""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="pysql")
cursor=connection.cursor()
cursor.execute("select * from table2 where id=1")
result=cursor.fetchall()
print("Content in the python :")
for x in result:
   print("\t",x) """







""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="pysql")
cursor=connection.cursor()
sql = "DELETE FROM table2 WHERE id=1"
cursor.execute(sql)
connection.commit()
print(cursor.rowcount, "record(s) deleted") """



'''import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="pysql")
cursor=connection.cursor()
sql = "DROP TABLE table2"
cursor.execute(sql)

import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
print(connection)

import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("create database newsql")

import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="newsql")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
    print(x)
import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="newsql")
cursor=connection.cursor()
cursor.execute("create table table1 (name varchar(255),age int)")
cursor.execute("show tables")
print("Number of tables in database :")
for x in cursor:
     print("\t",x)
import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="newsql")
cursor=connection.cursor()
s="insert into table1(name) values(%s)"
t=("Ajay")
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid)

import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="newsql")
cursor=connection.cursor()
s="insert into table1(name) values(%s)"
t=[("Hot"),("Cool")]
cursor.executemany(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid)

import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="newsql")
cursor=connection.cursor()
cursor.execute("select * from table1")
result=cursor.fetchall()
print("Content in the python :")
for x in result:
   print("\t",x)
import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="newsql")
cursor=connection.cursor()
sql = "DELETE FROM table1"
cursor.execute(sql)
connection.commit()
print(cursor.rowcount, "record(s) deleted") '''
import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="newsql")
cursor=connection.cursor()
sql="Drop Table table1"
cursor.execute(sql)








