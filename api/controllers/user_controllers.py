from api.models.user_models import User
from flask import jsonify, request

user_model = User()
user_model = admin()

class UsersController:
    
    def __init__(self):
        self.users = []

    def add_user(self, args):
        user = user_model.create_user(args)
        if not user:
            return jsonify({"message":"No user found"}), 200
        return jsonify({"status":201,"user":user}), 201

class AdminsController:
    def __init__(self):
        self.adminss = []

    def add_admin(self, args):
        admin = user_model.create_admin(args)
        if not admin:
            return jsonify({"message":"No admin user found"}), 200
        return jsonify({"status":201,"admin":admin}), 201
