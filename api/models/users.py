import jwt
from flask import jsonify, request
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from db.config import DatabaseConnection

conn = DatabaseConnection()


class User:
    # user class
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def signup(self, username, firstname, lastname, othernames, phoneNumber, isAdmin):
        # registering a new user
        user_exists = self.user_exists()

        if user_exists:
            response = jsonify({
                "message": "An account with that email already exists"
            })
            response.status_code = 409
            return response

        else:
            hashed_pw = generate_password_hash(self.password)

            conn.cur.execute(
                "INSERT INTO users(firstname, lastname, othernames, email, phoneNumber, username, password, isAdmin) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    firstname,
                    lastname,
                    othernames,
                    self.email,
                    phoneNumber,
                    username,
                    hashed_pw,
                    isAdmin))

            conn.cur.execute(
                "select id from users where email = '{}' ".format(
                    self.email))
            user_id = conn.cur.fetchone()
            token = self.generate_token(user_id)

            user_info = self.get_user_details()
            response = jsonify({
                "message": "User registered successfully",
                "token": token.decode("utf-8"),
                "user": user_info
            })
            response.status_code = 201
            return response

    def user_exists(self):
        # checking if user already exists
        conn.cur.execute("select * from users where email='{}'".format(self.email))
        user = conn.cur.fetchone()
        return user

    def get_user_details(self):
        # getting one user
        user = self.user_exists()
        return user
        response = jsonify({
            "message": "User not found"
        })
        response.status_code = 404
        return response

    def generate_token(self, user_id):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                'secret'
            )
        except Exception as e:
            return e

    def login(self):
        # logging in an existing user
        user_exists = self.user_exists()

        if user_exists:

            pw_match = check_password_hash(user_exists['password'], self.password)
            # (user_exists)

            if pw_match:
                token = self.generate_token(user_exists)

                user_info = self.get_user_details()

                response = jsonify({
                    "message": "Login successful",
                    "token": token.decode("utf-8"),
                    "user": user_info
                })
                response.status_code = 200
                return response

            else:
                response = jsonify({
                    "message": "Incorrect password"
                })
                response.status_code = 401
                return response

        else:
            response = jsonify({
                "message": "The email used is not registered. Try creating a new account"
            })
            response.status_code = 401
        return response
