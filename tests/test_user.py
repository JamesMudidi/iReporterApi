import unittest
import json
from api import app
from flask import Flask


class UserTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_signup(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "james@gmail.com",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "james"
        }
        response = self.client.post('api/v2/auth/signup',
        json=user)
        json.loads(response.data)
        self.assertEqual(response.status_code, 409)

    def test_email_already_exist(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "email@email.com",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user"
        }
        user1 = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "email@email.com",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user1"
        }
        self.client.post('api/v2/auth/signup',
        json=user)
        response = self.client.post('api/v2/auth/signup',
        json=user1)
        json.loads(response.data)
        self.assertEqual(response.status_code, 409)

    def test_email_exists(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "email1@email.com",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user1"
        }
        self.client.post('api/v2/auth/signup',
        json=user)
        response = self.client.post('api/v2/auth/signup',
        json=user)
        self.assertEqual(response.status_code, 409)

    def test_special_characters(self):

        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "`~!",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user1"
        }
        result = self.client.post('/api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_empty_email_signup(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user1"
        }
        result = self.client.post('/api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_empty_pass_signup(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "test@email.com",
            "password": "",
            "phoneNumber": "123455678",
            "username": "test_user1"
        }
        result = self.client.post('/api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_user_login(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "email@email.com",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user"
        }
        self.client.post('api/v2/auth/signup',
                         json=user)
        result = self.client.post('/api/v2/auth/login',
        data=json.dumps(user),
        content_type='application/json')
        print(result)
        self.assertEqual(result.status_code, 500)

    def test_email_format_signup(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "email",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user"
        }
        result = self.client.post('/api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_incorrect_email_login(self):
        result = self.client.post('/api/v2/auth/login',
        data=json.dumps(dict(
        email='wrong@email.com',
        password='pasword')),
        content_type='application/json')
        self.assertEqual(result.status_code, 401)

    def test_incorrect_password_login(self):
        result = self.client.post('/api/v2/auth/login',
        data=json.dumps(dict(
        email='sample@domain.com',
        password='password')),
        content_type='application/json')
        self.assertEqual(result.status_code, 401)

    def test_empty_email_login(self):
        result = self.client.post('/api/v2/auth/login',
        data=json.dumps({
        "email": '',
        "password": "password"}),
        content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_email_format_login(self):
        user_info = {
            "email": 'mail.com',
            "password": 'password'
        }
        result = self.client.post('/api/v2/auth/login',
        data=json.dumps(user_info),
        content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_get_all_users(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "email@email.com",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user"
        }
        self.client.post('api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json')
        response = self.client.post('api/v2/auth/login',
        data=json.dumps(user),
        content_type='application/json')
        result = self.client.get('/api/v2/users',
        headers=dict(Authorization=token),
        content_type='application/json')
        self.assertEqual(result.status_code, 500)

    def test_get_single_user(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "email@email.com",
            "password": "12345",
            "phoneNumber": "123455678",
            "username": "test_user"
        }
        self.client.post('api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json')
        response = self.client.post('api/v2/auth/login',
        data=json.dumps(user),
        content_type='application/json')
        result = self.client.get('/api/v2/users/1',
        headers=dict(Authorization=token),
        content_type='application/json')
        self.assertEqual(result.status_code, 500)

    def test_delete_user(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "authemail@email.com",
            "password": "12345555",
            "phoneNumber": "123455678",
            "username": "test_user69",
            "isAdmin": "True"
        }
        self.client.post('api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json')
        response = self.client.post('api/v2/auth/login',
        data=json.dumps(user),
        content_type='application/json')
        result = self.client.delete('/api/v2/users/2',
        headers=dict(Authorization=token),
        content_type='application/json')
        self.assertEqual(result.status_code, 401)

    def test_user_does_not_exist(self):
        user = {
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "othernames",
            "email": "authemail1@email.com",
            "password": "12345555",
            "phoneNumber": "123455678",
            "username": "test_user691",
            "isAdmin": "True"
        }
        self.client.post('api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json')
        response = self.client.post('api/v2/auth/login',
        data=json.dumps(user),
        content_type='application/json')
        result = self.client.delete('/api/v2/users/200',
        headers=dict(Authorization=token),
        content_type='application/json')
        self.assertEqual(result.status_code, 500)
