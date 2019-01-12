'''
Import relevant dependencies
datetime for the date and time
'''
import datetime
from flask import jsonify

# Create a list to save the created users
users=[]

# Defining model class for users
class User:
    def __init__(self):
        self.users=users

    def create_user(self, args):
        user=dict(
            userId=len(self.users)+1,
            firstName=args['firstName'],
            lastName=args['lastName'],
            otherNames=args['otherNames'],
            email=args['email'],
            phoneNumber=args['phoneNumber'],
            username=args['username'],
            registered=datetime.datetime.now(),
            isAdmin=False
        )
        self.users.append(user)
        return user

    def check_user_exists(userId, firstName, lastName, email):
        #check if a user is already in the system
        for user in user_list:
            return user['userId'] == userId
            return user['firstName'] == firstName
            return user['lastName'] == lastName
            return user['email'] == email