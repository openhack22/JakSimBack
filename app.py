from flask import Flask,request;
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/regist", methods = ['POST'])    # 회원가입.
def regist():
    user = request.form['user']                     # 아이디 중복 체크 넣어야함
    password = request.form['password']
    name = request.form['name']
    #print(request.form)
    #result = DBsetting.user_regist(user,password,name)
    #jsonresult = {
    #    'result' : result
    #}
    #resJson = json.dumps(jsonresult)
    #return resJson

@app.route("/login", methods = ['POST'])    # 로그인.
def login():
    user = request.form['user']
    password = request.form['password']
    #print(request.form)
    #userid = DBsetting.user_login(user,password)
    #jsonresult = {
    #    'id' : userid
    #}
    #jsonString = json.dumps(jsonresult)
    #print (jsonString)
    #return jsonString







if __name__ == '__main__':
    app.run()