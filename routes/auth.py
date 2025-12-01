import sqlite3

from flask import Flask, Blueprint, request, render_template,flash , url_for ,redirect

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
        conn.execute("INSERT INTO Users(username,password) values(?,?)",(username,password))
        conn.commit()
        conn.close()
        flash("Registration successful","success")
        return redirect(url_for("main.home"))


