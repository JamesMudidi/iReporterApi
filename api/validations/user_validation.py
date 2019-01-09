from flask import jsonify
import re

class validate_user:
    def validate_firstName(firstName):
        if not firstName or not isinstance(firstName, str) or firstName.isspace():
            return jsonify ({
                'status':400,
                'message':'firstName has to be filled with string characters only'}),400
        return True

    def validate_lastName(lastName):
        if not lastName or not isinstance(lastName, str) or lastName.isspace():
            return jsonify ({
                'status':400,
                'message':'lastName has to be filled with string characters only'}),400
        return True

    def validate_otherNames(otherNames):
        if not otherNames or not isinstance(otherNames, str) or otherNames.isspace():
            return jsonify ({
                'status':400,
                'message':'otherName has to be filled with string characters only'}),400
        return True

    def validate_email(email):
        if not email or not isinstance(email, str) or not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email) or email.isspace():
            return jsonify ({
                'status':400,
                'message':'email has to be filled correctly. example: user@domain.com'}),400
        return True

    def validate_phoneNumber(phoneNumber):
        if not phoneNumber or not isinstance(phoneNumber, str) or not re.match(r"[0-9]+", phoneNumber) or phoneNumber.isspace():
            return jsonify ({
                'status':400,
                'message':'phoneNumber has to be filled with numbers only'}),400
        return True

    def validate_username(username):
        if not username or not isinstance(username, str) or username.isspace():
            return jsonify ({
                'status':400,
                'message':'username has to be filled with string characters only'}),400
        return True

    def validate_password(password):
        if not password or len(password) < 8 or password.isspace():
            return jsonify ({
                'status':400,
                'message':'Invalid password, please provide a valid password longer than 8 characters'}),400
        return True

    def validate_registered(registered):
        if not registered or registered.isspace():
            return jsonify({
                'status':400,
                'message':'Invalid Date and Time'}),400
        return True

    def validate_isAdmin(isAdmin):
        if not isAdmin or not isinstance(isAdmin, bool) or isAdmin.isspace():
            return jsonify ({
                'status':400,
                'message':'isAdmin has to be a boolean'}),400
        return True