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
    phoneNmber = data.get('phoneNumber')
    password = data.get('password')

    user = Users(name, email, phoneNeumber, username, password)
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
        if user != None:
            if check_password_hash(user['password'], password) and user['username'] == username:
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
@jwt_required
def welcome():
    username = get_jwt_identity()

    return jsonify ({
        'message': f'{username}, Thank you for using Kengo\'s API.'
    })

@app.errorhandler(404)
def page_not_found(e):
    valid_urls = {
        'Signup': {'url': '/api/v1/signup', 'method(s)': 'POST', 'body': {'username': 'String', 'email': 'example@email.com', 'password': 'At least 8 characters.'}},
        'Login': {'url': '/api/v1/login', 'method(s)': 'POST', 'body': {'username': 'String', 'password': 'Enter user password.'}},
        'Welcome': {'url': '/api/v1/welcome', 'method(s)': 'GET', 'header': 'JWT access token.'}
    }
    return jsonify ({
        'Issue': 'You have entered an unknown URL.',
        'Valid URLs': valid_urls,
        'message': 'Please contact Kengo Wada for more details on this API.'
        })