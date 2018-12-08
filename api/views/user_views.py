# Import neccessary depencies
# From the module or framework, we import the class datatype.
# Using requst to add and access data
# Using jsonify to generate JSON data
# Using json for reading JSON data
from flask import Flask, jsonify, request, json
from api.controllers.user_controllers import UsersController
from api import app

user_controller = UsersController()

class user_views:  
    # Route for creating a user
    @app.route('/api/v1/users', methods=['POST'])
    def add_user():
        request_data = request.get_json()
        return user_controllers.add_user(request_data)

    # Route for selecting a single user
    @app.route('/api/v1/users/<int:_id>', methods=['GET'])
    def get_specific_user(_id):
        return user_controllers.get_specific_user(_id)

    # Route for selecting all users
    @app.route('/api/v1/users',methods=['GET'])
    def get_users():
        return user_controllers.get_all_users()

    # Route for deleting a user
    @app.route('/api/v1/users/<int:_id>',methods=['DELETE'])
    def delete_user(_id):
    return user_controllers.delete_user(_id)
