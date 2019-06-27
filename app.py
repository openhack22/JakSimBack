from flask import Flask, request, session
import module.sql_command as db
import json
from datetime import timedelta

app = Flask(__name__)
app.secret_ket = 'JaksimForever'

@app.route('/')
def hello_world():
    return 'Hello World!'


#@app.before_request
#def make_session_permanent():
#    session.permanent = True
#    app.permanent_session_lifetime = timedelta(minutes=60)


@app.route("/regist", methods = ['POST'])
def regist():
    """Regist ID Form"""
    id = request.form['id']
    password = request.form['password']
    username = request.form['username']
    #print(request.form)
    resDB = db.userRegist(id,password,username)
    jsonresult = {
        'result' : resDB
    }
    resJson = json.dumps(jsonresult)
    return resJson


@app.route("/login", methods = ['POST'])
def login():
    """Login Form"""
    id = request.form['id']
    password = request.form['password']
    resDB = db.userLogin(id,password)

    jsonResult = {
        'result' : resDB
    }
    jsonString = json.dumps(jsonResult)
    print (jsonString)
    return jsonString


@app.route("/logout")
def logout():
    """Logout Form"""
    id = request.form[id]
    return 200

@app.route("/setGoal")
def setGoal():
    id = request.form[id]

@app.route("/getList")
def getGoalList():
    """get Goal List Form"""
    id = request.form[id]

    resDB = db.getOnGoingList(id)
    print(resDB)
    #for tuple in resDB:
    jsonResult = {
        'result': resDB
    }

    #return resJson


if __name__ == '__main__':
    #db.createSchema()
    app.run(host='10.10.2.88', port = 5000, debug='True')


