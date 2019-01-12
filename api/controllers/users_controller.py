from api.models.user_model import User
from flask import jsonify, request

user_model = User()


class UsersController:
    
    def __init__(self):
        self.users = []


    def add_user(self, args):
        user =user_model.create_user(args)
        if not user:
            return jsonify({"message":"No user found"}), 200

        return jsonify({"status":201,"user":user}), 201

    

    
