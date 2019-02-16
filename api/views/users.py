from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
from marshmallow import ValidationError, Schema, fields
from db.config import DatabaseConnection
from api.models.users import User
from api.common.authenticator import authenticate
from api.common.validator import email, required
from api.views import api

conn = DatabaseConnection()

class SignUpSchema(Schema):
    # Represents the schema for users
    firstname = fields.Str(required=True, validate=(required))
    lastname = fields.Str(required=True, validate=(required))
    username = fields.Str(required=True, validate=(required))
    email = fields.Email(required=True, validate=(email))
    othernames = fields.Str(required=False)
    password = fields.Str(required=True, validate=(required))
    phoneNumber = fields.Str(required=True, validate=(required))
    isAdmin = fields.Str(required=False)


class SignInSchema(Schema):
    # Represents the schema for users
    email = fields.Email(required=True, validate=(email))
    password = fields.Str(required=True, validate=(required))


@api.route('/auth/signup', methods=['POST'])
def create_user():
    # creating a user
    conn = DatabaseConnection()

    data, errors = SignUpSchema().load(request.get_json())

    if errors:
        return jsonify({
            "message": errors,
            "status": 400}), 400

    conn.cur.execute("select * from users where username = '{}'".format(data['username']))
    user_names = conn.cur.fetchall()

    if len(user_names) > 0:
        response = jsonify({"message": "The username is already taken"})
        response.status_code = 409
        return response

    if email_exists(data['email']):
        response = jsonify(
            {"message": "The email is already taken"})
        response.status_code = 409
        return response

    if phone_exists(data['phoneNumber']):
        response = jsonify(
            {"message": "The Phone number is already taken"})
        response.status_code = 409
        return response

    user = User(data['email'], data['password'])

    if not data.get('isAdmin', '').strip():
        data['isAdmin'] = "False"

    register = user.signup(
        data['username'],
        data['firstname'],
        data['lastname'],
        data['othernames'],
        data['phoneNumber'],
        data['isAdmin']
    )

    return register

def email_exists(email):
    """ Check if a user exists in the db """
    conn = DatabaseConnection()
    conn.cur.execute("SELECT * from users WHERE email='{}'".format(email))
    user = conn.cur.fetchone()
    return user

def phone_exists(phoneNumber):
    """ Check if a user exists in the db """
    conn = DatabaseConnection()
    conn.cur.execute("SELECT * from users WHERE phoneNumber='{}'".format(phoneNumber))
    user = conn.cur.fetchone()
    return user

@api.route('/auth/login', methods=['POST'])
def login_user():
    # login in user
    data, errors = SignInSchema().load(request.get_json())

    if errors:
        return jsonify({
            "message": errors,
            "status": 400}), 400

    user = User(data['email'], data['password'])

    login = user.login()
    return login


@api.route('/users', methods=['GET'])
@authenticate
def get_users(identity):
    # getting all users
    conn = DatabaseConnection()
    conn.cur.execute("select * from users")
    users = conn.cur.fetchall()
    close_connection(conn)
    return jsonify({
        "data": users
    }), 200


@api.route('/users/<int:user_id>', methods=['GET'])
@authenticate
def get_one_user(identity, user_id):
    # getting one user
    conn = DatabaseConnection()
    conn.cur.execute("select * from users where id = {}".format(user_id))
    user_data = conn.cur.fetchone()
    close_connection(conn)
    return jsonify({
        "data": user_data
    }), 200


@api.route('/users/<int:user_id>', methods=['DELETE'])
@authenticate
def delete_user(identity, user_id):
    # deleting a user
    conn = DatabaseConnection()

    conn.cur.execute("select * from users where id = '{}'".format(user_id))
    users = conn.cur.fetchall()

    if not users:
        close_connection(conn)
        return jsonify({
            "message": "User does not exist"
        }), 200

    conn.cur.execute("delete from users where id = {}".format(user_id))
    conn.commit()
    close_connection(conn)
    return jsonify({
        "message": "User successfully deleted"
    }), 200



