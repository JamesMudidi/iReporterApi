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

        self.user0={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "james@mail.com",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

        self.user1={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "james@mail",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

        self.user2={
            "firstname": "",
            "lastname": "",
            "othernames": "",
            "email": "",
            "phoneNumber": "",
            "username": "",
            "registered": "",
            "password": "",
        }

        self.user3={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "james@mail.com",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "",
        }

        self.user4={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "james@mail.com",
            "phoneNumber": "123456789",
            "username": "",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

        self.user5={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

        self.user6={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "james@email.com",
            "phoneNumber": "",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

        self.user7={
            "firstname": "",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "james@email.com",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

        self.user8={
            "firstname": "James",
            "lastname": "",
            "othernames": "Jimmy",
            "email": "james@email.com",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

        self.user9={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "",
            "email": "james@email.com",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "12-01-2019 12:42",
            "password": "1234",
        }

        self.user10={
            "firstname": "James",
            "lastname": "Mudidi",
            "othernames": "Jimmy",
            "email": "james@email.com",
            "phoneNumber": "123456789",
            "username": "jimmy",
            "registered": "",
            "password": "1234",
        }

    def test_register_user(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_twice(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user)
        response = self.client.post('api/v1/users',
        json=self.user0)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_fields(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user2)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_wrong_email(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user1)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_password(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user3)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_username(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user4)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_email(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user5)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_phonenumber(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user6)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_firstname(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user7)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_lastname(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user8)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_othernames(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user9)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_register_user_with_empty_registered(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
        json=self.user10)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_get_all_users(self):
        # Tests that the end point fetches all users
        response = self.client.get('/api/v1/users',
        content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_get_users_not_exist(self):
        # Tests that the end point fetches all users
        response = self.client.get('/api/v1/users',
        json=self.user2)
        self.assertEqual(200, response.status_code)

    def test_get_user_details(self):
        # Tests that the end point returns a single user's details
        self.client.post('api/v1/users',
        json=self.user)
        response=self.client.get('/api/v1/users',
        content_type='application/json',
        json=self.user)
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_get_user_not_exist(self):
        self.client.post('api/v1/users',
        json=self.user2)
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
        self.assertIn("The ID provided is not in the system", msg['message'])
        self.assertEqual(400, response.status_code)

    def test_delete_user_not_exist(self):
        response = self.client.post('api/v1/users',
        content_type='application/json',
        json=self.user2)
        new_details = {}
        response = self.client.delete('api/v1/users/1',
        json=new_details)
        msg = json.loads(response.data)
        self.assertEqual(400, response.status_code)
