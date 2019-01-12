# Import neccessary depencies
# From the module or framework, we import the class datatype.
from flask import Flask, jsonify, request
app =Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	return jsonify(
        {'Application' : 'iRepoter'},
        {'1. Greetings': 'Welcome to the iRepoter API'},
        {'2. Help': 'For further assistance contact James Mudidi on mudidi.jimmy@gmail.com.',
        })

from api.views import incident_view
from api.views import user_view