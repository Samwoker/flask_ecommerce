
from flask import Flask
from routes.main import main_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

app.config["SECRET_KEY"] = "098bdvbqe7reqb0dkewmf39r91mcamef2129cms92333"


if __name__ == '__main__':
    app.run(debug=True)