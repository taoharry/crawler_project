#!usr/bin/env python
# coding:utf-8

import sys,os
reload(sys)
sys.setdefaultencode('utf8')
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from flask import Flask, request, sessions, render_template, templating, jsonify


from TaskData import TaskData, obj2dict
from TaskApi import TaskApi as api
from Content import tableWaite,tableDoing,tableFinish,waite_to_doing,doing_to_finish
app = Flask(__name__)
api = api()


client_lt = api.ShowClientType()
version_lt = api.ShowVersion()

@app.route('/addtask',methods=['GET','POST'])
def AddTask():
    task = TaskData()
    if request.method == "POST":
        task.taskType = request.form['taskType']
        task.taskId = request.form['taskId']
        task.channel = request.form['channel']
        task.descript = request.form['descript']
        task.interval = request.form['interval']
        task.version = request.form['version']
        task.priority = request.form['priority']
        task.duration = request.form['duration']
        task.clientType = request.form['clientType']
        task.path = request.form['path']
        task.data = request.form['data']
        #把数据放到waiting数据库里面
        data = obj2dict(task)
        r = api.InsertTask(data)
        return jsonify(r)
    if request.method == "GET":
        return render_template()


@app.route('/showversion',methods=['GET'])
def ShowVersion():
    #拿到是一个列表,列表里面有字典
    r = api.ShowVersion()
    return jsonify(r)

@app.route('/showclient',methods=['GET'])
def ShowClient():
    r = api.ShowClientType()
    return jsonify(r)

@app.route('/canceltask',methods=['GET','POST'])
def CancelTask():
    if request.method == 'POST':
        task_id = request.form.get('taskId','')
        r = api.CancelTask(task_id)
        return jsonify(r)
    else:
        return render_template('cancelTask.html')


@app.route('/getask',methods=['POST'])
def GEtTask():
    #如果是第一次就需要注册client和version表
    if 'version' not in request.form or 'clientType' not in request.form:
        return jsonify({'TypeErro':"From wrong"})
    version = request.form['version']
    clientType = request.form['clientType']
    length = request.form['length']
    def CheckAndRegister(checklt,checkkey,checkvalue,rqform = request.form):
        for dt in checklt:
            if dt[checkkey] == checkvalue:
                return
        checklt.update(rqform)
        if checkkey == "version":
            api.RegisterVersion(checkvalue)
        elif checkkey == "clientType":
            api.RegisterClientType()
    CheckAndRegister(version_lt,'version',version)
    CheckAndRegister(clientType,'clientType',clientType)
    data = api.GetTask(request.form)
    return data

@app.route('/finishtask',methods=['POST'])
def FinishTask():
    #如果是第一次就需要注册client和version表
    data = api.GetTask(request.form,tableDoing)
    return data

@app.route('/affirmtask',methods=['POST'])
def AffirmTask():
    reqfrom = request.form
    if "affirm" not in reqfrom and 'data' not in reqfrom:
        return jsonify({'TypeErro':"From wrong"})
    affirm = reqfrom['affirm']
    data = reqfrom['data']
    if affirm == waite_to_doing:
        r = api.AffirmTask(data,tableWaite,tableDoing)
    elif affirm == doing_to_finish:
        r = api.AffirmTask(data, tableDoing, tableFinish)
    return jsonify(r)

@app.roue('/getparasitiferip',methods=['GET'])
def GetParasitiferIp():
    ip = request.remote_addr
    return ip

@app.route('/login',methods=['GET','POST'])
def Login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        #检查名字和密码是否正确,密码需要哈希
    else:
        return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def Register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

@app.roue('/get',methods=['GET'])
def Get():
    arg = request.args
    if len(arg) != 0:
        return




if __name__ == "__main__":
    app.run(debug=True,port=22222)



