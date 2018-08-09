class Judgement:
    def if_signin(self,session):
        if session:
            uid = session['uid']
        else:
            session['uid'] = None
            session['username'] = None
            uid = None
        return uid

    def if_root(self,db,uid):
        if uid:
            root = execute_sql(db, "select root from user where id = "+str(uid), 'fetchone')
        else:
            root = [0]
        return root

    def allowed_file(self,filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
