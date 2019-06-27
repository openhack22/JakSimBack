#This is function module for database
import pymysql

conn = pymysql.connect(host='127.0.0.1', user = 'root', password = 'root', charset='utf8')
curs = conn.cursor()

def createSchema():
    global conn
    curs.execute('drop database if exists jaksim')
    conn.commit()
    curs.execute('create database jaksim')
    conn.commit()
    curs.execute("use jaksim")

    # Create User Table
    conn.cursor().execute('''create table user (
                              id varchar(45) primary key,
                              password varchar(25) not null,
                              username varchar(20) not null,
                              income int not null default 0,
                              outcome int not null default 0,
                              amount int not null default 0)
                            ''')
    conn.commit()

    # Create Goal Table
    conn.cursor().execute('''create table goal (
                              goal_id int auto_increment primary key,
                              goal_name varchar(45) not null,
                              duration int not null ,
                              amount int not null ,
                              user_limit int not null ,
                              money_stack int not null ,
                              status boolean not null,
                              description text)''')
    conn.commit()

    # Create Team Table
    conn.cursor().execute('''create table team (
                              goal_id int references goal(goal_id) on update cascade,
                              user_id varchar(45) references user(id) on update cascade,
                              date date,
                              image text,
                              PRIMARY KEY( goal_id, user_id, date ))''')
    conn.commit()


# Sign up
def userRegist(id,password,username):
    curs.execute("use jaksim")
    SQL_chk = 'SELECT * FROM User WHERE id = %s'
    curs.execute(SQL_chk, (id))
    n = curs.fetchone()
    if (n==None):
        SQL_regist = 'INSERT INTO user (id,password,username) VALUES (%s,%s,%s)'
        curs.execute(SQL_regist, (id, password,username))
        conn.commit()
        return 200
    else: return 400

# Sign in
def userLogin(id,password):
    curs.execute("use jaksim")
    SQL_user = 'SELECT * FROM User WHERE id = %s'
    curs.execute(SQL_user, (id))
    n = curs.fetchone()
    if( n == None):
        return 400
    elif password == n[1]:
        return 200
    else:
        return -100

# Return On Going List
def getOnGoingList(id):
    curs.execute("use jaksim")
    SQL_chk = 'SELECT * FROM Team WHERE user_name = %s'
    curs.execute(SQL_chk, (id))
    n = curs.fetchone()
