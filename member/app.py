from flask import Flask, render_template, request, redirect 
from models import db
import os
import hashlib
from models import Fcuser
app = Flask(__name__)

def hash_password(pw):
    md = hashlib.md5()
    md.update(pw.encode('utf-8'))
    ctext = md.hexdigest()
    print(ctext)
    return ctext

@app.route('/')
def hello():
    return render_template("hello.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        userid = request.form.get('userid') 
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        print(password)


        if not (userid and username and password and re_password) :
            return "fill all input field"
        elif password != re_password:
            return "password is not matched"
        else: 
            fcuser = Fcuser()         
            fcuser.password = hash_password(password)
            fcuser.userid = userid
            fcuser.username = username      
            db.session.add(fcuser)
            db.session.commit()
            return "success member regist"

        return redirect('/')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    db.create_all()


    app.run(host='127.0.0.1', port=5000, debug=True) 
