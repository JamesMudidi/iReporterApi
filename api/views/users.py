from flask import Flask, jsonify, request
from api.models.users import User
from datetime import datetime
from api.common.validator import email, required
from marshmallow import ValidationError, Schema, fields
from api.views import api

users = []


class UserSchema(Schema):
    # Represents the schema for users
    firstName = fields.Str(required=True, validate=(required))
    lastName = fields.Str(required=True, validate=(required))
    otherNames = fields.Str(required=True, validate=(required))
    userName = fields.Str(required=True, validate=(required))
    email = fields.Email(required=True, validate=(email))
    password = fields.Str(required=True, validate=(required))
    phoneNumber = fields.Int(required=True, validate=(required))


@api.route('/users', methods=['POST'])
def create_user():
    # creating a user
    data, errors = UserSchema().load(request.get_json())

    if errors:
        return jsonify({
            "errors": errors,
            "status": 422}), 422

    userId = len(users)+1
    registered = datetime.now().strftime('%d-%m-%Y %H:%M')
    isAdmin = False

    user = User(userId, data['firstName'], data['lastName'],
                data['otherNames'], data['email'], data['phoneNumber'],
                data['userName'], registered, isAdmin, data['password'])

    users.append(user)

    return jsonify({
        "User": user,
        "Message": "User created",
        "status": 201
        }), 201


@api.route('/users', methods=['GET'])
def get_users():
    # getting all users
    user = [user.get_user_details() for user in users]
    return jsonify({
        "User": user
        }), 200


@api.route('/users/<int:userId>', methods=['GET'])
# getting one user
def get_one_user(userId):
    one_user = []
    user = users[userId - 1]
    one_user.append(user.get_user_details())
    return jsonify({
        "data": one_user
        }), 200


@api.route('/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    # deleting a user
    if userId == 0 or userId > len(users):
        return jsonify({"message": "The ID provided is not in the system"}), 400
    for user in users:
        if userId == userId:
            users.remove(user)
    return jsonify({"message": "account successfully deleted"}), 200
