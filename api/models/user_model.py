'''
Import relevant dependencies
datetime for the date and time
'''
import datetime
from flask import jsonify

# Create a list to save the created users
users_list = []

# Defining model class for users
class User:
    users_list = []

    def __init__(self, userId, firstName, lastName, otherNames, email,
                phoneNumber, username, password, registered, isAdmin):
        self.userId=len(users_list)+1
        self.firstName=firstName
        self.lastName=lastName
        self.otherNames=otherNames
        self.email=email
        self.phoneNumber=phoneNumber
        self.username=username
        self.password=password
        self.registered=datetime.datetime.now()
        self.isAdmin=False

    def user_dict(self):
        users = {
             "userId":self.userId,
             "firstName":self.firstName,
             "lastName":self.lastName,
             "otherNames":self.otherNames,
             "email":self.email,
             "phoneNumber":self.phoneNumber,
             "username":self.username,
             "password":self.password,
             "registered":self.registered,
             "isAdmin":self.isAdmin
        }
        self.users_list.append(users)
        return jsonify({
            'status':200,
            'data':users,
            'message':'user successfully registered'
            })

    @staticmethod
    def check_user_exists(userId, firstName, lastName, username, email):
        #check if a user is already in the system
        for users in users_list:
            return users['userId'] == userId
            return users['firstName'] == firstName
            return users['lastName'] == lastName
            return users['username'] == username
            return users['email'] == email

# Defining model class for the admin user and inheriting the user class
class Admin(User):
    def __init__(self, userId, firstName, lastName, otherNames, email,
                phoneNumber, username, password, registered, isAdmin):
        super().__init__(userId, firstName, lastName, otherNames, email,
                phoneNumber, username, password, registered)
        self.isAdmin=True
