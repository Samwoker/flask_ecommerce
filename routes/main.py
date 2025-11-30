from flask import Flask ,Blueprint,request

main_bp = Blueprint('main',__name__)

@main_bp.route('/<string:username>',methods=["POST","GET"])
def home(username):
    print(username)
    if request.method == "GET":
        return f'Hello, {request.args.get("name")}, This is a get request'
    else:
        return f'{request.form.get("name")} is {request.form.get("age")} and he learns at {request.form.get("school")}'

@main_bp.route('/people')
def people():
    return "Samuel is here"


