#/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import os
from flask import Flask, jsonify


from crawler_project.utills.monggoSql import MonggoUtils
from crawler_project.utills.logUtiles import logUtils
from crawler_project.utills.timeUtils import formatToday

app = Flask(__name__)
log = logUtils()



@app.route('/<channel>/<location>/<sort>/<int:sortid>/<int:id>', methods=['GET'])
def hello_world(channel, location, sort,sortid,  id):
    #return 'Hello World!'
    newResault = []
    id = int(id)
    sortid = int(sortid)
    lt = formatFind(channel,location)
    for cha in lt:
        resalut = MonggoUtils().getDataToday(channel, cha, sortid, sort)
        for i in resalut:
            del i['_id']
            newResault.append(i)
    log.info('start flask_web')
    if id == 0:
        id =1
    elif id+10 > len(newResault):
        return jsonify(newResault[-10:])

    return jsonify(newResault[id:id+10])

def formatFind(location):
    lt = []
    location = location.split('_') if location != 'NoneFind' else 'NoneFind'
    monggofind = {"timeIn":formatToday}
    if location != 'NoneFind':
        for l in location:
            monggofind["location"] = {"$regex":location}
            lt.append(monggofind)
    else:
        lt.append(monggofind)
    return lt



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2018)
