#!/usr/bin/env python
from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'this a index'

#@app.route('/hello')
#def hello():
#    return 'this a test web!!!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/login')
def login(): pass


@app.route('/logout')
def logout(): pass

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
