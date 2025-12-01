from flask import Flask, Blueprint, request, render_template
import sqlite3

main_bp = Blueprint('main',__name__)

def get_db():
    conn = sqlite3.connect("test.db")
    conn.row_factory = sqlite3.Row
    return conn

@main_bp.route('/')
def home():
   conn = get_db()
   products = conn.execute("SELECT * FROM Products").fetchall()
   products = [dict(product) for product in products]
   return render_template('home.html',products=products)

@main_bp.route('/people')
def people():
    return "Samuel is here"


