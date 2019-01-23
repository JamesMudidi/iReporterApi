from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    '''404 Error function'''
    return (jsonify({'error': str(error)}), 404)


@app.errorhandler(400)
def bad_request(error):
    '''400 Error function'''
    return (jsonify({'error': str(error)}), 400)


@app.errorhandler(405)
def method_not_allowed(error):
    '''405 Error function'''
    return (jsonify({'error': str(error)}), 405)


@app.errorhandler(500)
def server_error(error):
    '''405 Error function'''
    return (jsonify({'error': str(error)}), 500)


@app.route('/', methods=['GET'])
def test():
    return jsonify(
        {'Application': 'iRepoter'},
        {'1. Greetings': 'Welcome to the iRepoter API'},
        {'2. Help': 'Contact James Mudidi on mudidi.jimmy@gmail.com.'}
    )


app.url_map.strict_slashes = False

from api.views import users, incident, api

app.register_blueprint(api, url_prefix='/api/v2')
