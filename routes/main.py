from flask import Flask, Blueprint, request, render_template

main_bp = Blueprint('main',__name__)

@main_bp.route('/',methods=["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        return f'{request.form.get("name")} is {request.form.get("age")} and he learns at {request.form.get("school")}'

@main_bp.route('/people')
def people():
    return "Samuel is here"


