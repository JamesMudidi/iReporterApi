from flask import Flask, jsonify, request, json
from api import app
from api.controllers.user_controller import UsersController

users_controller = UsersController()

@app.route('/api/v1/users', methods=['POST'])
def register_user():
    request_data = request.get_json()
    return users_controller.add_user(request_data) 
