# Import neccessary depencies
# From the module or framework, we import the class datatype.
# Using requst to add and access data
# Using jsonify to generate JSON data
from api.models.user_models import User
from api.validations.user_validations import Validate
from flask import jsonify, request

user_models = User()

# Defining controller class for users
class UsersController:
    def __init__(self):
        # Create a list to save the information generated
        self.users = []

    def add_user(self, args):
        user = user_model.create_user(args)
        if not user:
            return jsonify({"message":"No user found"}), 204
        return jsonify({"status":201,"user":user}), 201

    def get_specific_user(self, user_id):
        user = user_models.get_user(user_id)
        if not user:
            return jsonify({"status":204,"message": 
                "Given user ID is out of range"}),204
        return jsonify({"status":200,"data":user}),200
    
    def get_all_users(self):
        users = user_models.get_users()
        if not userss or len(users) < 1:
            return jsonify({"status":204,"message": "No Users available"}),204
        return jsonify({"status":200,"data":users})

    def delete_user(self, user_id):
        user = user_models.get_an_user(user_id)
        users = user_models.get_users()
        if user:
            users.remove(user)
            return jsonify({"status":200, "data":f'{user} item has been deleted'}),200
        return jsonify({"status":204, "message": "Given user ID is out of range"}),204
