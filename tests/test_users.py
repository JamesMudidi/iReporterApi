# import neccesary dependencies
import unittest
from flask import Flask
# from api import app
# from api.views import user_view
import json

app = Flask(__name__)

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app=app.test_client()

    def test_register_user(self):
        user={
            'userId':1,
            'firstName':'James',
            'lastName':'Mudidi',
            'otherNames':'Tukei',
            'email':'james@mail.com',
            'phoneNumber':'0759123456',
            'username':'James',
            'password':'password',
            'registered':'2019-01-09 06:24:',
            'isAdmin':False
            }
        self.app.post('/api/v1/users/signup',
        content_type= 'application/json',
        data = json.dumps(user))
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code,404)

    # def tearDown(self):
    #     users_list.clear()