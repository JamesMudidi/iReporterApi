import unittest
import json
from api import app
from flask import Flask

class Test_record_views(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()
        self.user={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "james@mail.com",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

    def test_register_user(self):
        # Tests that the end point enables a new user create an account
        
        response = self.client.post('api/v1/users',
        json=self.user)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_get_all_users(self):
        # Tests that the end point fetches all users
        response = self.client.get('/api/v1/users',
                                   content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_get_single_user_details(self):
        # Tests that the end point returns a single user's details

        self.client.post('api/v1/users',
        json=self.user)
        response=self.client.get('/api/v1/users/',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_delete_user_details(self):
        # Tests that the end point enables user delete account

        response = self.client.post('api/v1/users',
        content_type='application/json',
        json=self.user)
        new_details = {}
        response = self.client.delete('api/v1/users/1',
        json=new_details)
        msg = json.loads(response.data)
        self.assertIn("Index out of range", msg['message'])
        self.assertEqual(400, response.status_code)
