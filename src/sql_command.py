#This is function module for database
import pymysql

conn = pymysql.connect(host='localhost', user = 'root', password = '456123', db='test', charset='utf8')
curs = conn.cursor()

# Sign up
def userRegist(id,password,username):
    SQL_chk = 'SELECT * FROM User WHERE id = %s'
    curs.execute(SQL_chk, (id))
    n = curs.fetchone()
    if (n==None):
        SQL_regist = 'INSERT INTO user (id,password,username,0,0,0) VALUES (%s,%s,%s,%d,%d)'
        curs.execute(SQL_regist, (id, password,username))
        conn.commit()
        return 200
    else: return 400

# Sign in
def userLogin(id,password):
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
    SQL_chk = 'SELECT * FROM Team WHERE user_name = %s'
    curs.execute(SQL_chk, (id))
    n = curs.fetchone()
