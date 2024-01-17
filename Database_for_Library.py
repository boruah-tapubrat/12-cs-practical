import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",password="tapubrat56300*")

connect()
c1 = db1.cursor()
#c1.execute("drop database library")
c1.execute("create database library")
c1.execute("use library")
c1.execute("create table users (username varchar(30), password varchar(30))")
c1.execute("insert into users values('Debojit','786623')")
c1.execute("insert into users values('Tapubrat','xyz123')")
db1.commit()
c1.execute("create table member(Mid varchar(20) primary key,Name varchar(50),Email varchar(50), Phone varchar(20))")
c1.execute("create table books(bookid varchar(20) primary key,title varchar(50), author varchar(50), publisher varchar(50), cost integer)")
c1.execute("create table issue(mid varchar(20), bookid varchar(20), dateofissue date)")
c1.execute("create table issuelog(mid varchar(20), bookid varchar(20), dateofissue date, dateofreturn date)")
db1.commit()
db1.close()
