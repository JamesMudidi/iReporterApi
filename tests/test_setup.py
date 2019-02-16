import unittest
import json
from api import app


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        self.incident = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2"
        }
    def user_auth_token(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        user_details = {
            "firstname": "test_firstn",
            "lastname": "test_lastname",
            "othernames": "test_othernames",
            "email": "authemail@email.com",
            "password": "1234555",
            "phoneNumber": "12345678",
            "username": "test_user69",
        }
        self.client.post('api/v2/auth/signup',
        data=json.dumps(user_details),
        content_type='application/json')
        response = self.client.post('api/v2/auth/signup',
        data=json.dumps(user_details),
        content_type='application/json')
        user_jwt = json.loads(response.data.decode("utf-8"))['token']
        return user_jwt

    def admin_auth_token(self):
        ''' Register a new user '''

        user_details = {
            "firstname": "test_firstn",
            "lastname": "test_lastname",
            "othernames": "test_othernames",
            "email": "test_admin@email.com",
            "password": "1234555",
            "phoneNumber": "12345678",
            "username": "test_admin",
            "isAdmin": "True"
        }
        self.client.post('api/v2/auth/signup',
        data=json.dumps(user_details),
        content_type='application/json')
        response = self.client.post('api/v2/auth/login',
        data=json.dumps(user_details),
        content_type='application/json')
        user_jwt = json.loads(response.data.decode("utf-8"))['token']
        return user_jwt
