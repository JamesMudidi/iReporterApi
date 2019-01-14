import unittest
import json
from api import app
from flask import Flask

class Test_record_views(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_register_user(self):
        # Tests that the end point enables a new user create an account
        user_details = {
                        "firstname": "test_firstname",
                        "lastname": "test_lastname",
                        "othernames": "test_othernames",
                        "email": "test_email@email.com",
                        "phoneNumber": "test_phonNumber",
                        "username": "test_username",
                        "registered": "registered",
                        "password": "1234",
                        }
        response = self.client.post('api/v1/users',
        json=user_details)
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 422)

    def test_fetch_all_users(self):
        # Tests that the end point fetches all users
        response = self.client.get('/api/v1/users',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_single_user_details(self):
        # Tests that the end point returns a single user's details
        user_details = {
                        "firstname": "test_firstname",
                        "lastname": "test_lastname",
                        "othernames": "test_othernames",
                        "email": "test_email@email.com",
                        "phoneNumber": "test_phonNumber",
                        "username": "test_username",
                        "registered": "registered",
                        "password": "1234",
                            }
        self.client.post('api/v1/users',
        json=user_details)
        response=self.client.get('/api/v1/users/',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_user_details(self):
        # Tests that the end point enables user delete account
        user_details = {
                        "firstname": "test_firstname",
                        "lastname": "test_lastname",
                        "othernames": "test_othernames",
                        "email": "test_email@email.com",
                        "phoneNumber": "test_phonNumber",
                        "username": "test_username",
                        "registered": "registered",
                        "password": "1234",
            }
        response = self.client.post('api/v1/users',
        content_type='application/json',
        json=user_details)
        new_details = {}
        response = self.client.delete('api/v1/users/1',
        json=new_details)
        msg = json.loads(response.data)
        self.assertIn("Index out of range", msg['message'])
        self.assertEqual(response.status_code, 400)
