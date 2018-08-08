###下列为演示上传文字的代码###

from flask import Flask, request, render_template,url_for, session,redirect
from werkzeug.utils import secure_filename#此处flask文档有问题
from flask import send_from_directory
import pymysql
import os

UPLOAD_FOLDER = 'C:/programming/web/upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#rsplit函数提取后缀
# a in b：判断a是否在b中，若是，返回Ture，反之返回False
@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        #file存储的是图片名
        if file and allowed_file(file.filename):
            #file存储的是图片名的字符串格式
            filename = secure_filename(file.filename)
            #secure函数过滤掉非ASCII字符
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #os.path.join()将后一个参数的路径加入前一个
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template('test2.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    #send_from_directory内容：<response streamed [200 0k]>

if __name__ == '__main__':#确保本py文件仅在直接运行时执行下列代码，作为模块调用时不会执行测试代码
    app.run(debug=True)#用 run() 函数来让应用运行在本地服务器上