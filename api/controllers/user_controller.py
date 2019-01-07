'''
Import neccessary depencies
From the module or framework, we import the class datatype.
Using requst to add and access data
Using jsonify to generate JSON data
'''
from api.models.user_model import User
from flask import jsonify, request

user_model=User()

# Defining controller class for users
class UserController:
    def __init__(self):
        # Create a list to save the information generated
        self.user=[]

    def add_user(self, args):
        user=user_model.add_user(args)
        if not user:
            return jsonify({"message":"No users found. Add a new user"}),204
        return jsonify({"status":201,"user":user})