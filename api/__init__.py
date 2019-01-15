from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	return jsonify(
        {'Application' : 'iRepoter'},
        {'1. Greetings': 'Welcome to the iRepoter API'},
        {'2. Help': 'For further assistance contact James Mudidi on mudidi.jimmy@gmail.com.',
        })

app.url_map.strict_slashes = False

from api.views import users, incident, api

app.register_blueprint(api, url_prefix='/api/v1')