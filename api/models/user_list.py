from api.models.models import User 
from flask import Flask, jsonify
import json

user_list = []
class UserList:

    def __init__(self):
        self.user_list = user_list

    def add_new_user(self, id, firstname, lastname,
                     othername, email, phone_number, username,
                     registered, is_admin):
        user = {
            "id":len(self.user_list)+1,
            "firstname":firstname,
            "lastname":lastname,
            "othername":othername,
            "email":email,
            "phone_number":phone_number,
            "username":username,
            "registered":registered,
            "is_admin":is_admin
        }
        user_list.append(user)
        # return user


    def retreave_users(self):
        return user_list

