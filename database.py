import mysql.connector as pymysql

def create_table():
    con=pymysql.connect(host='localhost',user='Faith',password='@Faith4real')
    mycursor=con.cursor()
    mycursor.execute('use tutorial') 
    mycursor.execute('create table if not exists registration(id int primary key,name varchar(50),duration varchar(50),format varchar(50),language varchar(50),price varchar(50))')
    con.commit()
    con.close()

def insert_courses(id,name,duration,format,language,price):
    con=pymysql.connect(host='localhost',user='Faith',password='@Faith4real')
    mycursor=con.cursor()
    mycursor.execute('use tutorial') 
    mycursor.execute('insert into registration(id,name,duration,format,language,price)values(%d,%s,%s,%s,%s,%d)',(id,name,duration,format,language,price))
    con.commit()
    con.close()

def search_course(query):
    con=pymysql.connect(host='localhost',user='Faith',password='@Faith4real')
    mycursor=con.cursor()
    mycursor.execute('use tutorial') 
    mycursor.execute('select* from registration where id=%s',(query))
    row=mycursor.fetchone()
    con.close()
    return row

def fetch_all_ids():
    con=pymysql.connect(host='localhost',user='Faith',password='@Faith4real')
    mycursor=con.cursor()
    mycursor.execute('use tutorial') 
    mycursor.execute('select id from registration')
    ids=mycursor.fetchall()
    con.close()
    return[i[0] for i in ids] 

def id_exist(id):
    con=pymysql.connect(host='localhost',user='Faith',password='@Faith4real')
    mycursor=con.cursor()
    mycursor.execute('use tutorial') 
    mycursor.execute('select count(*) from registration where id=%s',(id))
    result=mycursor.fetchone()
    con.close()
    return result[0]>0


create_table()                                                                 