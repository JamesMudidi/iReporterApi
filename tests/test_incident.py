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

        self.data0={
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

        self.data1={
            "id" : "",
            "createdOn" : "",  
            "createdBy" : "", 
            "type" : "",       
            "location" : "",   
            "status" : "",     
            "comment" : "",
            "Images" : "",
            "Videos" : ""
        }

        self.data2={
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

        self.data3={
            "id" : "",
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }

        self.data4={
            "id" : 1,
            "createdOn" : "",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }

        self.data5={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }

        self.data6={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }

        self.data7={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }

        self.data8={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : "videos"
        }

        self.data9={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "",
            "Images" : "images",
            "Videos" : "videos"
        }

        self.data10={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "",
            "Videos" : "videos"
        }

        self.data11={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it starts here",
            "Images" : "images",
            "Videos" : ""
        }

        self.data12={
            "id" : 1,
            "createdOn" : "12-01-2019 12:42",  
            "createdBy" : "James", 
            "type" : "redflag",       
            "location" : "Kampala",   
            "status" : "draft",     
            "comment" : "it is urgent",
            "Images" : "images",
            "Videos" : "videos"
        }

    def test_create_incident(self):
        response = self.client.post('/api/v1/incident',
        json = self.data)
        msg = json.loads(response.data)
        self.assertEqual(201, response.status_code)

    def test_create_incident_with_empty_fields(self):
        response = self.client.post('/api/v1/incident',
        json = self.data1)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_incident_with_empty_id(self):
        response = self.client.post('/api/v1/incident',
        json = self.data3)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_incident_with_empty_type(self):
        response = self.client.post('/api/v1/incident',
        json = self.data6)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_incident_with_empty_location(self):
        response = self.client.post('/api/v1/incident',
        json = self.data7)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_incident_with_empty_comment(self):
        response = self.client.post('/api/v1/incident',
        json = self.data9)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_incident_twice(self):
        response = self.client.post('/api/v1/incident',
        json = self.data)
        response = self.client.post('/api/v1/incident',
        json = self.data1)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_get_incidents(self):
        # Tests that the end point fetches all records
        response = self.client.get('/api/v1/incident',
        content_type = 'application/json')
        self.assertEqual(200, response.status_code)

    def test_get_incidents_not_exists(self):
        response = self.client.post('/api/v1/incident',
        json = self.data)
        response = self.client.get('/api/v1/incident',
        content_type = 'application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_get_single_incident(self):
        # Tests that the end point returns a single record
        self.client.post('/api/v1/incident',
        json = self.data)
        response = self.client.get('/api/v1/incident/1',
        content_type = 'application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_get_incident_not_exists(self):
        self.client.post('/api/v1/incident',
        json = self.data)
        response = self.client.get('/api/v1/incident/1',
        json = self.data1)
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_delete_incident(self):
        # Tests that the end point enables user edit an incident
        # record when rejected by admin
        response = self.client.post('/api/v1/incident',
        content_type = 'application/json',
        json = self.data)
        new_details = {}
        response = self.client.delete('/api/v1/incident/1',
        json = new_details)
        msg = json.loads(response.data)
        self.assertIn("incident successfully deleted", msg['message'])
        self.assertEqual(200, response.status_code)

    def test_delete_incident_not_exists(self):
        # Tests that the end point enables user edit an incident
        # record when rejected by admin
        response = self.client.post('/api/v1/incident',
        content_type = 'application/json',
        json = self.data1)
        new_details = {}
        response = self.client.delete('/api/v1/incident/0',
        json = new_details)
        msg = json.loads(response.data)
        self.assertEqual(400, response.status_code)

    def test_create_redflag(self):
        response = self.client.post('/api/v1/redflag',
        json = self.data)
        msg = json.loads(response.data)
        self.assertEqual(201, response.status_code)

    def test_create_redflag_with_empty_fields(self):
        response = self.client.post('/api/v1/redflag',
        json = self.data1)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_redflag_with_empty_id(self):
        response = self.client.post('/api/v1/redflag',
        json = self.data3)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_redflag_with_empty_type(self):
        response = self.client.post('/api/v1/redflag',
        json = self.data6)
        msg = json.loads(response.data)
        self.assertEqual(201, response.status_code)

    def test_create_redflag_with_empty_location(self):
        response = self.client.post('/api/v1/redflag',
        json = self.data7)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_redflag_with_empty_comment(self):
        response = self.client.post('/api/v1/redflag',
        json = self.data9)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_create_redflag_not_exists(self):
        response = self.client.post('/api/v1/redflag',
        json = self.data1)
        msg = json.loads(response.data)
        self.assertEqual(422, response.status_code)

    def test_get_redflags(self):
        # Tests that the end point fetches all records
        response = self.client.get('/api/v1/redflag',
        content_type = 'application/json')
        self.assertEqual(200, response.status_code)

    def test_get_single_redflag(self):
        # Tests that the end point returns a single record
        self.client.post('/api/v1/redflag',
        json = self.data)
        response = self.client.get('/api/v1/redflag',
        content_type = 'application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_get_redflag_not_exists(self):
        self.client.post('/api/v1/redflag',
        json = self.data1)
        response = self.client.get('/api/v1/redflag',
        content_type = 'application/json')
        msg = json.loads(response.data)
        self.assertEqual(200, response.status_code)

    def test_delete_redflag(self):
        # Tests that the end point enables user edit an incident
        # record when rejected by admin
        response = self.client.post('/api/v1/redflag',
        content_type = 'application/json',
        json = self.data)
        redflag = {}
        response = self.client.delete('/api/v1/redflag/1',
        json = redflag)
        msg = json.loads(response.data)
        self.assertIn("redflag successfully deleted", msg['message'])
        self.assertEqual(200, response.status_code)

    # def test_patch_redflag_location(self):
    #     self.client.post('/api/v1/redflag/1/location',
    #     json = self.data)
    #     response = self.client.patch('/api/v1/redflag/1/location',
    #     json = self.data12)
    #     msg = json.loads(response.data)
    #     self.assertIn("redflag location updated", msg['message'])
    #     self.assertEqual(200, response.status_code)

    def test_delete_redflag_not_exists(self):
        response = self.client.post('/api/v1/redflag',
        content_type='application/json',
        json = self.data1)
        new_details = {}
        response = self.client.delete('/api/v1/redflag/0',
        json = new_details)
        msg = json.loads(response.data)
        self.assertEqual(400, response.status_code)

