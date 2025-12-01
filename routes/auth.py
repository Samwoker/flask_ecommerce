import sqlite3

from flask import Flask, Blueprint, request, render_template, flash, url_for, redirect, session

auth_bp = Blueprint('auth',__name__)


def get_db():
    conn = sqlite3.connect("test.db")
    conn.row_factory = sqlite3.Row
    return conn

@auth_bp.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if len(password) < 8 :
            flash("Password should be at least 8 characters","error")
            return redirect(url_for("auth.signup"))
        conn = get_db()
        try:
            conn.execute("INSERT INTO Users(username,password) values(?,?)",(username,password))
            conn.commit()
        except sqlite3.IntegrityError:
            flash("Username is taken please enter another","error")
            return redirect(url_for("auth.signup"))
        finally:
            conn.close()
        flash("Registration successful","success")
        return redirect(url_for("auth.login"))

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conn = get_db()
        user = conn.execute("SELECT * from Users where username = ?",(username,)).fetchone()
        if user and password == user['password']:
            session['username'] = username
            flash("Logged in successfully")
            return redirect(url_for("main.home"))
        flash("Invalid username or password","error")
        conn.close()
        return redirect(url_for("auth.login"))

@auth_bp.route("/logout")
def logout():
    session.pop('username',None)
    flash("Successfully logged out")
    return redirect(url_for('auth.login'))
