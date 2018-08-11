from flask import Flask, request, render_template,url_for, session,redirect
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pymysql
import os
from function import open_db,close_db,execute_sql,if_signin,allowed_file,if_root,id_name_get,description_get
#导入了 Flask 类，这个类的实例（app）是 WSGI 应用程序
#导入render_template函数，可以返回html文档
UPLOAD_FOLDER = 'C:/programming/web/static/upload'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
#使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数，即将url与函数绑定
def home():
    uid = if_signin(session)
    db = open_db()
    cities = id_name_get(db)
    close_db(db)
    return render_template('newchina.html', username = session['username'],uid = uid,cities = cities)

@app.route('/area/<cityid>', methods=['GET', 'POST'])
def area(cityid):
    uid = if_signin(session)
    db = open_db()
    content = execute_sql(db, "select id,name,description,picture from city where id = '"+cityid+"'", 'fetchall')
    root = if_root(db,uid)
    cities = id_name_get(db)
    close_db(db)
    return render_template('area.html',cities = cities,username = session['username'],content = content,cityid = cityid,root = root[0],uid = uid)

@app.route('/signin', methods=['GET'])
def SigninForm():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])#登陆成功ajax修改
def Signin():
    username = request.form['username']
    password = request.form['password']
    db = open_db()
    if len(username) <= 20 and 7 <=len(password) <= 20:
        data = execute_sql(db, "select id, username, password from user where username = '" + username + "'", 'fetchall')
        close_db(db)
        if data and password == data[0][2]:
            session['uid'] = data[0][0]
            session['username'] = data[0][1]
            return "success"
        return "fault"
    else:
        close_db(db)
        return "outOfRange"

app.secret_key = '111111'





@app.route('/reg', methods=['GET'])
def reg_form():
    return render_template('reg.html')


@app.route('/reg', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    db = open_db()
    if len(username) <= 20 and 7 <= len(password) <= 20:
        execute_sql(db, "insert into user (username, password,root) values('"+ username + "', '" + password +"','0')", 'insert')
        uid = execute_sql(db, "select id from user where username = '" + username + "'", 'fetchone')
        close_db(db)
        session['username'] = username
        session['uid'] = uid[0]
        return "success"
    else:
        close_db(db)
        return "outOfRange"

app.secret_key = '111111'

@app.route('/signoff', methods=['GET'])#ajax修改
def signoff():
    session.clear()
    return redirect(url_for('home'))

@app.route('/area/<cityid>/modification', methods=['GET'])
def modify(cityid):
    uid = if_signin(session)
    db = open_db()
    description = description_get(db,cityid)
    root = if_root(db,uid)
    close_db(db)
    return render_template('modification.html',description = description,username = session['username'],cityid = cityid,root = root[0])

@app.route('/area/<cityid>/modification', methods=['POST'])
def modification(cityid):
    modification = request.form['description']
    db = open_db()
    execute_sql(db, "UPDATE city SET description = '"+modification+"'WHERE id = '"+cityid+"'", 'update')
    close_db(db)
    return "success"

@app.route('/area/<cityid>/upload', methods=['GET'])
def upload_get(cityid):
    return render_template('upload.html',cityid = cityid)

@app.route('/area/<cityid>/upload', methods=['POST'])
def upload_post(cityid):
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    db = open_db()
    execute_sql(db, "UPDATE city SET picture = '"+filename+"'WHERE id = '"+cityid+"'",'update')
    close_db(db)
    return render_template('upload-process.html',cityid = cityid,filename = filename)

if __name__ == '__main__':#确保本py文件仅在直接运行时执行下列代码，作为模块调用时不会执行测试代码
    app.run(debug=True)#用 run() 函数来让应用运行在本地服务器上


'''
@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('process.html',state = "sign")

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    db = open_db()
    if len(username) <= 20 and 7 <=len(password) <= 20:
        data = execute_sql(db, "select id, username, password from user where username = '" + username + "'", 'fetchall')
        close_db(db)
        print(session['username'])
        if data and password == data[0][2]:
            session['uid'] = data[0][0]
            session['username'] = data[0][1]
            return render_template('process.html', username = session['username'])
        return render_template('process.html', state = "sign_wrong_data")
    else:
        close_db(db)
        return render_template('process.html', state = "out_of_range")

@app.route('/reg', methods=['GET'])
def reg_form():
    return render_template('process.html',state = "reg")


@app.route('/reg', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    db = open_db()
    if len(username) <= 20 and 7 <= len(password) <= 20:
        execute_sql(db, "insert into user (username, password,root) values('"+ username + "', '" + password +"','0')", 'insert')
        uid = execute_sql(db, "select id from user where username = '" + username + "'", 'fetchone')
        close_db(db)
        session['username'] = username
        session['uid'] = uid[0]
        return render_template('process.html',username = username)
    else:
        close_db(db)
        return render_template('process.html',state = "out_of_range")

app.secret_key = '111111'
'''