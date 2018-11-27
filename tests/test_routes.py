import unittest
from api.routes import app
import json


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()

    def test_user_register(self):
        user = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        response  = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['message'], 'James successfully registered.')
    
    def test_register_username_twice(self):
        user1 = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user1)
        )

        user2 = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        response2  = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user2)
        )

        message = json.loads(response2.data.decode())

        self.assertEqual(message['message'], 'Username is taken.')

    def test_register_email_twice(self):
        user1 = {
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user1)
        )

        user2 = {
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        response2  = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user2)
        )

        message = json.loads(response2.data.decode())

        self.assertEqual(message['message'], 'Email already has an account.')

    def test_register_empty_username(self):
        user = {
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        response  = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['Error'], 'Username field can not be left empty.')

    def test_register_empty_email(self):
        user = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        response  = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['Error'], 'Email field can not be left empty.')

    def test_register_empty_password(self):
        user = {
            'id' : 1,
            'name' : 'james',
            'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
            'username' : 'james',
            'password' : ''
        }

        response  = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['Error'], 'Password field can not be left empty.')

    def test_register_invalid_email(self):
        user = {
            'id' : 1,
            'name' : 'james',
            'email' : 'jamesgmail.com',
			'phoneNumber' : '0701234567',
            'username' : 'james',
            'password' : 'password'
        }

        response  = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['Error'], 'Enter a valid email address.')

    def test_register_password_length(self):
        user = {
            'id' : 1,
            'name' : 'james',
            'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
            'username' : 'james',
            'password' : 'pas'
        }

        response  = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['Error'], 'Password has to be longer than 4 characters.')

    def test_user_login(self):
        user1 = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user1)
        )

        user = {
            'username': 'james',
            'password': 'password'
        }

        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['message'], 'james successfully logged in.')

    def test_user_login_empty_username(self):
        user1 = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user1)
        )

        user = {
            'username': '',
            'password': 'password'
        }

        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['Error'], 'Username field can not be left empty.')

    def test_user_login_empty_password(self):
        user1 = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user1)
        )

        user = {
            'username': 'james',
            'password': ''
        }

        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['Error'], 'Password field can not be left empty.')
    
    def test_login_wrong_username(self):
        user1 = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user1)
        )

        user = {
            'username': 'mudidi',
            'password': 'password'
        }

        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['message'], 'Wrong login credentials.')

    def test_login_wrong_password(self):
        user1 = {
			'id' : 1,
			'name' : 'james',
			'email' : 'james@gmail.com',
			'phoneNumber' : '0701234567',
			'username' : 'james',
			'password' : 'password'
        }

        self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user1)
        )

        user = {
            'username': 'james',
            'password': 'passworld'
        }

        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['message'], 'Wrong login credentials.')
    