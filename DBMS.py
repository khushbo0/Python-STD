import pymysql as p
from flask import *

def getConnection():
    db= p.connect(host='localhost',user='root',password='',database='pythondbms')
    return db
print(getConnection())

def insertData(t):
    db=getConnection()
    cr=db.cursor()
    sql='insert into std values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllStd():
    db=getConnection()
    cr=db.cursor()
    sql='select * from std'
    cr.execute(sql)
    slist=cr.fetchall()
    db.commit()
    db.close()
    return slist

def deleteData(id):
    db=getConnection()
    cr=db.cursor()
    sql='delete from std where id=%s'
    cr.execute(sql,id)
    db.commit()
    db.close()
    
def selectStdById(id):
    db=getConnection()
    cr=db.cursor()
    sql='select * from std where id=%s'
    cr.execute(sql,id)
    slist=cr.fetchall()
    db.commit()
    db.close()
    return slist[0]

def updateData(t):
    db=getConnection()
    cr=db.cursor()
    sql='update std set name=%s,fathername=%s,mothername=%s,course=%s,contact=%s,address=%s,email=%s,password=%s where id=%s'
    cr.execute(sql,t)
    db.commit()
    db.close()

 
def editData(id):
    db=getConnection()
    cr=db.cursor()
    sql='edit from std where id=%s'
    cr.execute(sql,id)
    db.commit()
    db.close()
