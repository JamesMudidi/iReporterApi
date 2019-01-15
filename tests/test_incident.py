import unittest
import json
from api import app

class test_incident(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_incident(self):
        incident=[]
        response=self.client.post(
        '/api/v1/incident',
        content_type='application/json')
        data={
            "id" : 1,
            "createdOn" : "Date",  
            "createdBy" : "James", 
            "type" : "red-flags",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }
        incident.append(data)
        response=self.client.get('/api/v1/incident',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_incidents(self):
        # Tests that the end point fetches all records
        response=self.client.get('/api/v1/incident',
        content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_incident(self):
        # Tests that the end point returns a single record
        incident_details = {
            "id" : 1,
            "createdOn" : "Date",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
            }
        self.client.post('/api/v1/incident',
        json=incident_details)
        response = self.client.get('/api/v1/incident',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_incident(self):
        # Tests that the end point enables user edit an incident
        # record when rejected by admin
        incident_details = {
            "id" : 1,
            "createdOn" : "Date",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
            }
        response = self.client.post('/api/v1/incident',
        content_type='application/json',
        json=incident_details)
        new_details = {}
        response = self.client.delete('/api/v1/incident/1',
        json=new_details)
        msg = json.loads(response.data)
        self.assertIn("Index out of range", msg['message'])
        self.assertEqual(response.status_code, 400)


    def test_create_redflag(self):
        incident=[]
        response=self.client.post(
        '/api/v1/redflag',
        content_type='application/json')
        data={
            "id" : 1,
            "createdOn" : "Date",  
            "createdBy" : "James", 
            "type" : "red-flags",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }
        incident.append(data)
        response=self.client.get('/api/v1/incident',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_redflags(self):
        # Tests that the end point fetches all records
        response=self.client.get('/api/v1/incident',
        content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_redflag(self):
        # Tests that the end point returns a single record
        redflag = {
            "id" : 1,
            "createdOn" : "Date",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
            }
        self.client.post('/api/v1/redflag',
        json=redflag)
        response = self.client.get('/api/v1/redflag',
        content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_redflag(self):
        # Tests that the end point enables user edit an incident
        # record when rejected by admin
        redflag = {
            "id" : 1,
            "createdOn" : "Date",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
            }
        response = self.client.post('/api/v1/redflag',
        content_type='application/json',
        json=redflag)
        redflag = {}
        response = self.client.delete('/api/v1/redflag/1',
        json=redflag)
        msg = json.loads(response.data)
        self.assertIn("redflag successfully deleted", msg['message'])
        self.assertEqual(response.status_code, 200)
