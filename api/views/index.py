# Import neccessary depencies
# From the module or framework, we import the class datatype.
from flask import Flask, jsonify, request
import json
from api import app

# Defining what displays in the default route
# Default error page
@app.route('/', methods=['GET'])

# Defining what displays in the default route
def index():
    return jsonify(
        {'Status' : 200,
        'Application' : 'iRepoter'},
        {
        '1. Greetings': 'Welcome to the iRepoter API',
        '2. Help': 'For further assistance contact James Mudidi on mudidi.jimmy@gmail.com.',
        }
        ), 200