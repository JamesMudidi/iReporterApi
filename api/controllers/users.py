from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
from marshmallow import ValidationError, Schema, fields
from db.config import DatabaseConnection
from api.models.users import User
from api.common.authenticator import authenticate
from api.common.validator import email, required
from api.views import api

class users:
	def email_exists(email):
	    """ Check if a user exists in the db """
	    conn = DatabaseConnection()
	    conn.cur.execute("SELECT * from users WHERE email='{}'".format(email))
	    user = conn.cur.fetchone()
	    return user

