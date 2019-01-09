# import neccesary dependencies
from flask import Flask
import unittest
# from api import app
# from api.views import incident_view
import json

app = Flask(__name__)

class TestIncidents(unittest.TestCase):
    def setUp(self):
        self.app=app.test_clent()

    # def tearDown(self):
    # incidents_list.clear()