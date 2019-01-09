'''
Import neccessary depencies
From the module or framework, we import the class datatype.
Using requst to add and access data
Using jsonify to generate JSON data
'''
from flask import jsonify, request, json
from api.models import user_model
from api.validations import user_validation

class User_controller:
    def add_user(userType):
        data=request.get_json()

        userId=len(users_list)+1
        firstName=data.get('firstName')
        lastName=data.get('lastName')
        otherNames=data.get('otherNames')
        email=data.get('email')
        phoneNumber=data.get('phoneNumber')
        username=data.get('username')
        password=data.get('password')
        registered=datetime.datetime.now()
        isAdmin=False

        if not firstName:
            return jsonify({
                'status':400,
                'error':'firstName has to be filled with string characters only'
                })
        if not lastName:
            return jsonify({
                'status':400,
                'error':'lastName has to be filled with string characters only'
                })
        if not otherNames:
            return jsonify({
                'status':400,
                'error':'otherName has to be filled with string characters only'
                })
        if not email:
            return jsonify({
                'status':400,
                'error':'email has to be filled with string characters only'
                })
        if not phoneNumber:
            return jsonify({
                'status':400,
                'error':'phoneNumber has to be filled with string characters only'
                })
        if not username:
            return jsonify({
                'status':400,
                'error':'username has to be filled with string characters only'
                })
        if not password:
            return jsonify({
                'status':400,
                'error':'password has to be filled with string characters only'
                })

        if not validate_user.validate_firstName:
            return jsonify({
                'status':400,
                'error':'firstName has to be filled with string characters only'
                })
        if not validate_user.validate_lastName:
            return jsonify({
                'status':400,
                'error':'lastName has to be filled with string characters only'
                })
        if not validate_user.validate_otherNames:
            return jsonify({
                'status':400,
                'error':'otherName has to be filled with string characters only'
                })
        if not validate_user.validate_email:
            return jsonify({
                'status':400,
                'error':'email has to be filled correctly. example: user@domain.com'
                })
        if not validate_user.validate_phoneNumber:
            return jsonify({
                'status':400,
                'error':'phoneNumber has to be filled with numbers only'
                })
        if not validate_user.validate_username:
            return jsonify({
                'status':400,
                'error':'username has to be filled with numbers only'
                })
        if not validate_user.validate_password:
            return jsonify({
                'status':400,
                'error':'Invalid password, please provide a valid password longer than 8 characters'
                })

        if isAdmin=='False':
            user=User(firstName, lastName, otherNames,
                email, phoneNumber, username, password)
            if User.check_user_exists(userId, firstName, lastName, username, email):
                return jsonify({
                'status':200,
                'user':user,
                'message':'User account already exists with these details'
                })
        elif isAdmin=='True':
            user=User(firstName, lastName, otherNames,
                email, phoneNumber, username, password)
            if User.check_user_exists(userId, firstName, lastName, username, email):
                return jsonify({
                'status':200,
                'user':user,
                'message':'User account already exists with these details'
                })
        else:
            return jsonify({
                'error':'Invalid user type',
                'status':400
                }),400
