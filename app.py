from flask import Flask, request, session
import module.sql_command as db
import json

app = Flask(__name__)
app.secret_ket = 'JaksimForever'

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/regist", methods = ['POST'])
def regist():
    """Regist ID Form"""

    print( "/resist  <- ")
    print(request.get_json())
    data = request.get_json()
    id = data['id']
    password = data['password']
    username = data['username']
    resDB = db.userRegist(id, password, username)
    jsonresult = {
        'result' : resDB
    }
    resJson = json.dumps(jsonresult)
    print("/resist  ->")
    print(resJson)
    return resJson


@app.route("/login", methods=['POST'])
def login():
    """Login Form"""
    print("/login  <- ")
    print(request.get_json())
    data = request.get_json()
    id = data['id']
    password = data['password']
    resDB = db.userLogin(id, password)
    jsonResult = {
        'username' : resDB
    }
    resJson = json.dumps(jsonResult)
    print("/resist  -> ")
    print(resJson)
    return resJson


@app.route("/checkID", methods = ['POST'])
def checkID():
    print("/checkID  <- ")
    print(request.get_json())
    data = request.get_json()
    id = data['id']
    resDB = db.chkID(id)
    jsonResult = {
        'result': resDB
    }
    resJson = json.dumps(jsonResult)
    print("/checkID  -> ")
    print(resJson)
    return resJson

@app.route("/logout" , methods = ['POST'])
def logout():
    """Logout Form"""
    print("/logout  <- ")
    print(request.get_json())
    data = request.get_json()
    id = data['id']
    jsonResult = {
        'result': 200
    }
    resJson = json.dumps(jsonResult)
    print("/logout  -> ")
    print(resJson)
    return resJson

@app.route("/addRoom", methods = ['POST'])
def addRoom():
    print("/addRoom <- ")
    print(request.get_json())
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
    resJson = json.dumps(jsonResult)
    print("/addRoom  <- ")
    print(resJson)
    return resJson


@app.route("/getMyList" , methods = ['POST'])
def getMyList():
    """get Goal List Form"""
    print("/getMyList  <- ")
    print(request.get_json())
    data = request.get_json()
    id = data['id']

    resDB = db.getMyList(id)
    for tuple in resDB:
        print(tuple)
    #for tuple in resDB:
    jsonResult = {
        'result': 200
    }
    resJson = json.dumps(jsonResult)
    print("/resJson  -> ")
    print(resJson)
    return resJson


@app.route("/getWatingList", methods=['POST'])
def getWatingList():
    """get Goal List Form"""
    print("/getWatingList  <- ")
    print( request.get_json())
    data = request.get_json()
    duration = data['duration']
    resDB = db.getWatingList(duration)
    for tuple in resDB:
        print(tuple)

    # for tuple in resDB:

    jsonResult = {
        "goal_id" : [x[0] for x in resDB],
        "goal_name" : [x[1] for x in resDB ],
        "user_id" : [x[2] for x in resDB ],
        "duration": [x[3] for x in resDB],
        "amount": [x[4] for x in resDB],
        "user_limit": [x[5] for x in resDB],
        "description": [x[6] for x in resDB],
    }
    resJson = json.dumps(jsonResult)
    print("/getWatingList  -> ")
    print(resJson)
    return resJson


@app.route("/joinRoom", methods=['POST'])
def joinRoom():
    """User joing room funciton"""
    print("/joinRoom  <- ")
    print(request.get_json())
    data = request.get_json()
    user_id = data['id']
    jsonResult = {
        "result" : "asdf"
    }
    resJson = json.dumps(jsonResult)
    print("/joinRoom  -> ")
    print(resJson)
    return resJson


if __name__ == '__main__':
    #db.createSchema()
    app.run(host='10.10.2.88', port = 5000, debug = True)


