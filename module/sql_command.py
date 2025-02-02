#This is function module for database
import pymysql
import datetime

goal_id = 0
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
                              amount int not null default 0,
                              bank varchar(20) default null,
                              cardnum varchar(45) default null,
                              cvc varchar(3) default null,
                              carddue date default null,
                              cardpassword varchar(45) default null
                            ) DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;
                            ''')
    conn.commit()

    # Create Goal Table
    conn.cursor().execute('''create table goal (
                              goal_id int primary key,
                              goal_name varchar(20) not null,
                              user_id varchar(45) not null,
                              duration int not null ,
                              amount int not null ,
                              user_limit int not null ,
                              description text,
                              status boolean not null default 0
                              ) DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;
                              ''')
    conn.commit()

    # Create Team Table
    conn.cursor().execute('''create table team (
                              goal_id int references goal(goal_id) on update cascade,
                              goal_name varchar(20) not null,
                              user_id varchar(45) references user(id) on update cascade,
                              date datetime,
                              image text,
                              comment text,
                              status boolean not null default 0,
                              PRIMARY KEY( goal_id, user_id, date )
                              ) DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;
                              ''')
    conn.commit()


def chkID(id):
    curs.execute("use jaksim")
    SQL_chk = 'SELECT * FROM User WHERE id = %s'
    curs.execute(SQL_chk, (id))
    n = curs.fetchone()
    if (n == None):
        return 200
    else:
        return 400

# Sign up
def userRegist(id , password, username, bank = None, cardnum = None, cvc = None, carddue = None, cardpassword = None):
    curs.execute("use jaksim")
    SQL_chk = 'SELECT * FROM User WHERE id = %s'
    curs.execute(SQL_chk, (id))
    n = curs.fetchone()
    if (n==None):
        if bank != None:
            SQL_regist = 'INSERT INTO user (id,password, username, bank, cardnum, cvc, carddue, cardpassword) VALUES (%s,%s,%s, %s, %s,%s,%s, %s)'
            curs.execute(SQL_regist, (id, password, username, bank, cardnum, cvc, carddue, cardpassword))
        else :
            SQL_regist = 'INSERT INTO user (id,password,username) VALUES (%s,%s,%s)'
            curs.execute(SQL_regist, (id, password, username))
        conn.commit()
        return 200
    else:
        return 400

# Sign in
def userLogin(id,password):
    curs.execute("use jaksim")
    SQL_user = 'SELECT * FROM user WHERE id = %s'
    curs.execute(SQL_user, (id))
    n = curs.fetchone()
    if( n == None):
        return 400
    elif password == n[1]:
        return n[2]
    else:
        return -100

# Return On Going List
def getMyGoalList(id):
    curs.execute("use jaksim")
    SQL_chk = 'SELECT * FROM Team WHERE user_name = %s'
    curs.execute(SQL_chk, (id))
    n = curs.fetchone()


def getMyList(user_id):
    curs.execute("use jaksim")
    SQL_user = 'SELECT DISTINCT * FROM team WHERE user_id = %s'
    curs.execute(SQL_user, (user_id))
    n = curs.fetchall()
    limit = []
    cnt = []
    for item in n:
        goal_id = item[0]
        SQL_select = 'SELECT user_limit FROM goal WHERE goal_id = %s'
        curs.execute(SQL_select, (goal_id))
        user_limit = curs.fetchone()[0]
        limit.append(user_limit)

        SQL_select = 'SELECT count(*) FROM team WHERE goal_id = %s and user_id = %s GROUP BY user_id'
        curs.execute(SQL_select, (goal_id,user_id))
        count = curs.fetchone()[0]
        cnt.append(count)

    return n, limit, cnt

def getWatingList(duration):
    curs.execute("use jaksim")
    SQL_watingList = 'SELECT * FROM goal WHERE status = 0 and duration = %s'
    curs.execute(SQL_watingList, (duration))
    n = curs.fetchall()
    return n

def addRoom(user_ID, goalName,goalDescription, duration, amount, user_limit):
    curs.execute("use jaksim")
    curs.execute('SELECT goal_id FROM goal ORDER BY goal_id DESC')
    goal_id = curs.fetchone()
    if goal_id == None:
        goal_id = 1
    else :
         goal_id = goal_id[0] + 1
    SQL_goal_regist = 'INSERT INTO goal (goal_id, goal_name, user_id, duration, amount, user_limit, description) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    curs.execute(SQL_goal_regist, (str(goal_id), goalName, user_ID, duration, amount, user_limit, goalDescription))
    conn.commit()

    SQL_team_regist = 'INSERT INTO Team (goal_id,goal_name, user_ID, date) VALUES (%s, %s, %s, %s)'
    now = datetime.datetime.now()
    curs.execute(SQL_team_regist, (str(goal_id), goalName,user_ID, now))
    conn.commit()
    return goal_id


def joinRoom(user_id, goal_id):
    curs.execute("use jaksim")
    SQL_limit = 'SELECT user_limit, goal_name  FROM goal WHERE goal_id = %s'
    curs.execute(SQL_limit, (goal_id))
    goal_info = curs.fetchone()
    SQL_goal = 'SELECT DISTINCT user_id  FROM team WHERE goal_id = %s'
    curs.execute(SQL_goal, (goal_id))
    people = curs.fetchall()

    if len(people) >= goal_info[0]:
        return 400

    now = datetime.datetime.now()
    SQL_join = 'INSERT INTO team (goal_id, goal_name, user_id, date) VALUE(%s,%s,%s,%s) '
    curs.execute(SQL_join, ( goal_id, goal_info[1], user_id, now ))
    conn.commit()
    return 200

def getRank(goal_id):
    curs.execute("use jaksim")
    SQL_search = 'SELECT user_id, count(*) ' \
                 'FROM team ' \
                 'WHERE goal_id  = %s ' \
                 'GROUP BY user_id ' \
                 'ORDER BY COUNT(*) DESC'
    curs.execute(SQL_search, (goal_id))
    n = curs.fetchall()
    return n

def getGoalInfo(goal_id):
    curs.execute("use jaksim")
    SQL_goal = 'SELECT * FROM goal where goal_id = %s'
    curs.execute(SQL_goal, (goal_id))
    goal_info = curs.fetchone()
    SQL_search = 'SELECT user_id FROM team WHERE goal_id  = %s'
    curs.execute(SQL_search, (goal_id))
    n = curs.fetchall()
    user_id = [x[0] for x in n]
    return goal_info, len(n), user_id

def start(goal_id):
    curs.execute("use jaksim")
    SQL_set = 'UPDATE goal set status = 1  where goal_id = %s'
    curs.execute(SQL_set, (goal_id))
    conn.commit()
    SQL_set = 'UPDATE team set status = 1  where goal_id = %s'
    curs.execute(SQL_set, (goal_id))
    conn.commit()
    return 200

def win(goal_id, user_id):
    curs.execute("use jaksim")
    SQL_set = 'UPDATE goal set status = 100  where goal_id = %s and user_id = %s'
    curs.execute(SQL_set, (goal_id,user_id))
    conn.commit()
    SQL_set = 'UPDATE team set status = 100  where goal_id = %s and user_id = %s'
    curs.execute(SQL_set, (goal_id, user_id))
    conn.commit()
    goal_info = getGoalInfo(goal_id)
    price =  int(goal_info[0][4]) * ( int(goal_info[1]) -1 )
    return price


def lose(goal_id, user_id):
    curs.execute("use jaksim")
    SQL_set = 'UPDATE goal set status = -1  where goal_id = %s and user_id = %s'
    curs.execute(SQL_set, (goal_id, user_id))
    conn.commit()
    SQL_set = 'UPDATE team set status = -1  where goal_id = %s and user_id = %s'
    curs.execute(SQL_set, (goal_id, user_id))
    conn.commit()
    goal_info = getGoalInfo(goal_id)
    price = -int(goal_info[0][4])
    return price