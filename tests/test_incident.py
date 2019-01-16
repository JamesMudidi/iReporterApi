import unittest
import json
from api import app

class test_incident(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.data={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }

    def test_create_incident(self):
        incident=[]
        response=self.client.post(
        '/api/v1/incident',
        content_type='application/json')
        
        incident.append(self.data)
        response=self.client.get('/api/v1/incident',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_get_incidents(self):
        # Tests that the end point fetches all records
        response=self.client.get('/api/v1/incident',
        content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_get_single_incident(self):
        # Tests that the end point returns a single record
        self.client.post('/api/v1/incident',
        json=self.data)
        response = self.client.get('/api/v1/incident',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_delete_incident(self):
        # Tests that the end point enables user edit an incident
        # record when rejected by admin
        response = self.client.post('/api/v1/incident',
        content_type='application/json',
        json=self.data)
        new_details = {}
        response = self.client.delete('/api/v1/incident/1',
        json=new_details)
        msg = json.loads(response.data)
        self.assertIn("incident successfully deleted", msg['message'])
        self.assertEqual(200, response.status_code)


    def test_create_redflag(self):
        incident=[]
        response=self.client.post(
        '/api/v1/redflag',
        content_type='application/json')

        incident.append(self.data)
        response=self.client.get('/api/v1/incident',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_get_redflags(self):
        # Tests that the end point fetches all records
        response=self.client.get('/api/v1/incident',
        content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_get_single_redflag(self):
        # Tests that the end point returns a single record

        self.client.post('/api/v1/redflag',
        json=self.data)
        response = self.client.get('/api/v1/redflag',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_delete_redflag(self):
        # Tests that the end point enables user edit an incident
        # record when rejected by admin

        response = self.client.post('/api/v1/redflag',
        content_type='application/json',
        json=self.data)
        redflag = {}
        response = self.client.delete('/api/v1/redflag/1',
        json=redflag)
        msg = json.loads(response.data)
        self.assertIn("redflag successfully deleted", msg['message'])
        self.assertEqual(200, response.status_code)
