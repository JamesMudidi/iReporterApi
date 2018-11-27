from flask import Flask, jsonify, request
import json
from api.models import Users

app = Flask(__name__)

@app.route('/api/v1/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    username = data.get('username')
    phoneNumber = data.get('phoneNumber')
    password = data.get('password')

    user = Users(self.name)
    error = user.validate_input()
    exists = user.check_user_exist()

    if not error:
        if not exists:
            password_hash = generate_password_hash(password, method='sha256')
            token = create_access_token(username)
            return jsonify({
                'access_token': token,
                'message': f'{username} successfully registered.'
                }), 201
        else:
            return jsonify({'message': exists}), 401
    else:
        return jsonify({'Error': error}), 400


@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    error = Users.login_validate(username, password)

    if not error:
        if username != None:
            if user['password'] == password and user['username'] == username:
                token = create_access_token(username)
                return jsonify ({
                    'access_token': token,
                    'message': f'{username} successfully logged in.'
                }), 200
            else:
                return jsonify ({'message': 'Wrong login credentials.'}), 400
        else:
            return jsonify ({'message': 'Wrong login credentials.'}), 400
    else:
        return jsonify({'Error': error}), 400


@app.route('/api/v1/welcome')
def welcome():
    username = get_jwt_identity()

    return jsonify ({
        'message': f'{username}, Welcome to iRepoter\'s API.'
    })

@app.errorhandler(404)
def page_not_found(e):
    valid_urls = {
        'Signup': {'url': '/api/v1/signup', 'method(s)': 'POST', 'body': {'name': 'String', 'email': 'example@email.com', 'username': 'String', 'phoneNumber': 'String', 'password': 'At least 4 characters.'}},
        'Login': {'url': '/api/v1/login', 'method(s)': 'POST', 'body': {'username': 'String', 'password': 'Enter user password.'}},
        'Welcome': {'url': '/api/v1/welcome', 'method(s)': 'GET', 'header': 'JWT access token.'}
    }
    return jsonify ({
        'Issue': 'You have entered an unknown URL.',
        'Valid URLs': valid_urls,
        'message': 'Please contact iRepoter for more details on this API.'
        })