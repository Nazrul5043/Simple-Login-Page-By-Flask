from flask import Flask, redirect, url_for, request,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def login():
    return render_template("login.html")
@app.route('/auth',methods=["POST"])
def auth():
    if request.method == 'POST':
      user = request.form['username']
      userpass = request.form['pass']
      if user == 'admin' and userpass == '1234':
          return render_template("home.html")
      else:
          return render_template("login.html",error ="authentication failed")
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)
