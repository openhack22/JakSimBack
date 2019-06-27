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
    print("Check THis OUt ")
    print( request.get_json())
    data = request.get_json()
    id = data['id']
    password = data['password']
    username = data['username']
    resDB = db.userRegist(id, password, username)
    jsonresult = {
        'result' : resDB
    }
    resJson = json.dumps(jsonresult)
    return resJson


@app.route("/login", methods=['POST'])
def login():
    """Login Form"""
    data = request.get_json()
    id = data['id']
    password = data['password']
    resDB = db.userLogin(id, password)
    jsonResult = {
        'username' : resDB
    }
    jsonString = json.dumps(jsonResult)
    print (jsonString)
    return jsonString


@app.route("/checkID", methods = ['POST'])
def checkID():
    data = request.get_json()
    id = data['id']
    resDB = db.chkID(id)
    jsonResult = {
        'result': resDB
    }
    jsonString = json.dumps(jsonResult)
    print(jsonString)
    return jsonString

@app.route("/logout" , methods = ['POST'])
def logout():
    """Logout Form"""
    data = request.get_json()
    id = data['id']
    jsonResult = {
        'result': 200
    }
    jsonString = json.dumps(jsonResult)
    print(jsonString)
    return jsonString

@app.route("/addRoom", methods = ['POST'])
def addRoom():
    data = request.get_json()
    id = data['id']
    goal_name = data['goalName']
    goal_description = data['goalDescription']
    duration = data['duration']
    cost = data['money']
    user_limit = data['userNum']
    resDB = db.addRoom(id, goal_name, goal_description, duration, cost, user_limit)
    jsonResult = {
        'result': resDB
    }
    jsonString = json.dumps(jsonResult)
    print(jsonString)
    return jsonString


@app.route("/getMyList" , methods = ['POST'])
def getMyList():
    """get Goal List Form"""
    data = request.get_json()
    id = data['id']
    print(id)
    resDB = db.getMyList(id)
    for tuple in resDB:
        print(tuple)
    #for tuple in resDB:
    jsonResult = {
        'result': 200
    }
    jsonString = json.dumps(jsonResult)
    print(jsonString)
    return jsonString


if __name__ == '__main__':
  #  db.createSchema()
    app.run(host='10.10.2.88', port = 5000, debug = True)


