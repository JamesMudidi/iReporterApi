# Import neccessary depencies
# Using re's pattern to match and find other strings or sets of strings
from api.models.user_models import User
from flask import Flask, jsonify, request, json
import re

class Validate:
    def validate_names(self):
        if not self.firstname or self.firstname.isspace():
            return jsonify({"status": 400,
                "message": "Firstname field can not be left empty."})
        return isinstance(firstname, str)

        if not self.lastname or self.lastname.isspace():
            return jsonify({"status": 400,
                "message": "Lastname field can not be left empty."})
        return isinstance(lastname, str)

    def validate_contact(self):
        if not self.email or self.email.isspace():
            return jsonify({"status": 400,
                "message": "Email field can not be left empty."})

        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return jsonify({"status": 400,
                "message": "Enter a valid email address."})

        elif not self.phone_number or self.phone_number.isspace():
            return jsonify({"status": 400,
                "message": "Phone number field can not be left empty."})
        return isinstance(phone_number, int)

    def validate_security(self):
        if not self.username or self.ussername.isspace():
            return jsonify({"status": 400,
                "message": "Username field can not be left empty."})

        elif not self.password or self.password.isspace():
            return jsonify({"status": 400,
                    "message": "Password field can not be left empty."})

        elif len(self.password) < 8:
            return jsonify({"status": 400,
                "message": "Password has to be longer than 8 characters."})
    
    def check_user_exist(self):
        if username is not None:
            return jsonify({"status": 400,
                "message": "Username is taken."})
        if email != None:
            return jsonify({"status": 400,
                "message": "Email already has an account."})
        if phone_number is not None:
            return jsonify({"status": 400,
                "message": "Phone number is taken."})

    @staticmethod
    def login_validate(username, password):
        if not username or username.isspace():
            return jsonify({"status": 400,
                "message": "Username field can not be left empty."})
        elif not password or password.isspace():
            return jsonify({"status": 400,
                "message": "Password field can not be left empty."})
        else:
            return False