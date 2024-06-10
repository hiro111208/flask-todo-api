from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app import app, mongo
from models import User


def initialize_routes(app):

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if mongo.db.users.find_one({'username': username}):
            return jsonify({"msg": "User already exists"}), 400
        user = User(username, password)
        mongo.db.users.insert_one({
            'username': user.username,
            'password': user.password
        })
        return jsonify({"msg": "User registered successfully"}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = mongo.db.users.find_one({'username': username})
        if not user or not User.check_password(user['password'], password):
            return jsonify({"msg": "Invalid credentials"}), 401
        access_token = create_access_token(identity=str(user['_id']))
        return jsonify(access_token=access_token), 200
