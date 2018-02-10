#!usr/bin/env python
# coding:utf-8

import sys,os
reload(sys)
sys.setdefaultencode('utf8')
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from flask import Flask, request, sessions, render_template, templating


from Searver_task_data import TaskData, obj2dict
from config.config import dbWaite
from utills.monggoSql import MonggoUtils
app = Flask(__name__)
waite = MonggoUtils(db=dbWaite)


@app.route('/',methods=['GET','POST'])
def sedTask():
    task = TaskData()
    if request.method == "POST":
        task.taskType = request.form['taskType']
        task.channel = request.form['channel']
        task.jobId = request.form['jobId']
        task.version = request.form['version']
        task.priority = request.form['priority']
        task.duration = request.form['duration']
        task.data = request.form['data']
        #把数据放到waiting数据库里面
        data = obj2dict(task)
        waite.insertOne(data)
    return



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        #检查名字和密码是否正确,密码需要哈希
    else:
        return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

@app.roue('/get',methods=['GET'])
def get():
    arg = request.args
    if len(arg) != 0:
        return



if __name__ == "__main__":
    app.run(debug=True)



