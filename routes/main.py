from flask import Flask, Blueprint, request, render_template, session,flash,redirect,url_for
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

@main_bp.route('/cart')
def cart():
    if 'username' not in session:
        flash("You are not logged in","error")
        return redirect(url_for('auth.login'))

@main_bp.route('/add-to-cart/<int:product_id>',methods=["POST","GET"])
def add_to_cart(product_id):
    if 'username' not in session:
        flash("You are not logged in","error")
        return redirect(url_for('auth.login'))
    conn = get_db()
    user = conn.execute('SELECT * FROM Users where username = ?',(session['username'],)).fetchone()
    if not user:
        flash('user not found','error')
        conn.close()
        return redirect(url_for('auth.login'))
    cart_item= conn.execute("SELECT * FROM Cart where user_id = ? and product_id = ?",(user['id'],product_id)).fetchone()
    if cart_item:
        conn.execute("UPDATE Cart SET quantity = quantity + 1 where id = ?",(cart_item['id'],))
    else:
        conn.execute("INSERT INTO Cart(user_id,product_id,quantity) VALUES (?,?,?)",(user['id'],product_id,1))
    conn.commit()
    conn.close()
    return redirect(url_for('main.home'))

@main_bp.route('/cart/update/<int:cart_id>',methods=["POST"])
def update_cart(cart_id):
    if 'username' not in session:
        flash("You are not logged in","error")
        return redirect(url_for('auth.login'))
    quantity = request.form.get("quantity",type=int)
    if quantity is None or quantity < 1:
        flash("Invalid quantity number","error")
        return redirect(url_for('main.cart'))
    conn = get_db()
    user = conn.execute("SELECT * FROM Users WHERE username = ?",(session['username'],)).fetchone()
    if not user:
        flash("User not found","error")
        conn.close()
        return redirect(url_for('auth.login'))
    conn.execute("UPDATE Cart SET quantity = ? where id = ? and user_id = ? ",(quantity,cart_id,user['id']))
    conn.commit()
    conn.close()
    flash("Cart updated successfully","success")
    return redirect(url_for('main.cart'))
