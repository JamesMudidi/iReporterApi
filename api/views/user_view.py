'''
Import neccessary depencies
From the module or framework, we import the class datatype.
Using requst to add and access data
Using jsonify to generate JSON data
Using json for reading JSON data
'''
from flask import Flask, jsonify, request, json
from api.controllers.user_controller import UserController
from api import app

user_controller = UserController()

class user_views:  
    # Route for creating a user
    @app.route('/api/v1/auth/users/signup', methods=['POST'])
    def register_user():
        data=request.get_json()
        return user_controller.add_user(data)
