import unittest
from api import app

class BaseTestCase(unittest.TestCase):
   
    def setUp(self):
        self.app = app.test_client()
        self.incident=dict(
            createdOn = "11-26-2018",
            createdBy = "Turinawe Smith",
            type = "red-flag",
            location = '0.3972� N, 32.6387� E',
            status = "draft",
            image = ["Image","Image"],
            video = ["Image","Image"],
            comment = "I was sked for a bribe to access servics at the HCIV"
            )
        self.incidents_empty = []
        self.incidents=[self.incident,self.incident]