from flask import Flask, request, render_template,url_for, session,redirect
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pymysql
import os
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def open_db():
    return pymysql.connect(host='localhost',user='root',password='jiangly1999',database='aaa',charset='utf8' )

def close_db(db):
    db.close()
        
    #创建一个该类的实例，第一个参数是应用模块或者包的名称
def execute_sql(db, sql, command):
    cursor = db.cursor()
    cursor.execute(sql)
    if command == 'fetchone':
        data = cursor.fetchone()
    elif command == 'fetchall':
        data = cursor.fetchall()
    elif command == 'insert' or 'update':
        db.commit()
        data = 0
    cursor.close()
    return data

def if_signin(session):
    if session:
        uid = session['uid']
    else:
        session['uid'] = None
        session['username'] = None
        uid = None
    return uid


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def if_root(db,uid):
    if uid:
        root = execute_sql(db, "select root from user where id = "+str(uid), 'fetchone')
    else:
        root = [0]
    return root

def id_name_get(db):
    return execute_sql(db, "select id,name from city", 'fetchall')

def description_get(db,cityid):
    description = execute_sql(db, "select description from city where id = '"+cityid+"'",'fetchone')
    return description[0]



