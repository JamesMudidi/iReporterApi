'''
Import neccessary depencies
From the module or framework, we import the class datatype.
Using requst to add and access data
Using jsonify to generate JSON data
Using json for reading JSON data
'''
from flask import Flask, jsonify, request, json
from api import app
from api.controllers import user_controller

class user_views:  
    # Route for creating a user
    @app.route('/api/v1/auth/users/signup', methods=['POST'])
    def register_user():
        data=request.get_json()
        return user_controller.add_user(data)

    # Route for creating an admin user
    @app.route('/api/v1/auth/admin/signup', methods=['POST'])
    def register_admin():
        data=request.get_json()
        return user_controller.add_user(data)

    # Route for user signin
    @app.route('/api/v1/auth/users/signin', methods=['POST'])
    def signin():
        data=request.get_json()
        username=data.get('username')
        password=data.get('password')
        if username==data.get('username') and password==data.get('password'):
            return jsonify({
                'status':200,
                'message':f'{username}, welcome to the iRepoter API'
                })

    # Route for admin signin
    @app.route('/api/v1/auth/admin/signin', methods=['POST'])
    def admin_signin():
        data=request.get_json()
        username=data.get('username')
        password=data.get('password')
        if username==data.get('username') and password==data.get('password'):
            return jsonify({
                'status':200,
                'message':f'{username}, welcome to the admin pannel of the iRepoter API'
                })