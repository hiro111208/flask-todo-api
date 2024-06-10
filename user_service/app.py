from routes import initialize_routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)

initialize_routes(app)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
