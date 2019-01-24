import unittest
import json
from api import app
from tests.test_setup import BaseTest


class Test_Incident(BaseTest):

    def test_add_redflag(self):
        response = self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(self.incident))
        self.assertEqual(response.status_code, 401)

    def test_add_intervention(self):
        response = self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(self.incident))
        self.assertEqual(response.status_code, 401)

    def test_get_single_redflag(self):
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(self.incident))
        response = self.client.get('api/v2/redflags/14',
        content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_get_single_intervention(self):
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(self.incident))
        response = self.client.get('api/v2/interventions/13',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_get_all_redflags(self):
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(self.incident))
        response = self.client.get('api/v2/redflags',
        content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_get_all_interventions(self):
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(self.incident))
        response = self.client.get('api/v2/interventions',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_empty_redflag_location(self):
        redflag = {
            "id": "1",
            "location": "",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        self.client.patch('api/v2/redflags/1/location',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.get('api/v2/redflags',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_empty_redflag_location(self):
        redflag = {
            "id": "1",
            "location": "",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        self.client.patch('api/v2/redflags/1/location',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.get('api/v2/redflags',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_empty_redflag_status(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        self.client.patch('api/v2/redflags/1/location',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.get('api/v2/redflags',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_empty_redflag_location(self):
        redflag = {
            "id": "1",
            "location": "",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        self.client.patch('api/v2/redflags/1/location',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.get('api/v2/redflags',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_redflag_location(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        self.client.patch('api/v2/redflags/1/location',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.get('api/v2/redflags',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_redflag_location(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        self.client.patch('api/v2/redflags/1/location',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.get('api/v2/redflags',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_redflag_location_empty(self):
        redflag = {
            "id": "1",
            "location": "",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        self.client.patch('api/v2/redflags/1/location',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.get('api/v2/redflags',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_intervention_location(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(intervention))
        self.client.patch('api/v2/interventions/1/location',
        content_type='application/json',
        data=json.dumps(intervention))
        response = self.client.get('api/v2/interventions',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_intervention_location_empty(self):
        intervention = {
            "id": "1",
            "location": "",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(intervention))
        self.client.patch('api/v2/interventions/1/location',
        content_type='application/json',
        data=json.dumps(intervention))
        response = self.client.get('api/v2/interventions',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_redflag_comment(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/8/comment',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_redflag_comment_empty(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "what we do",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/8/comment',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_redflag_comment_empty(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/8/comment',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_intervention_comment(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(intervention))
        response = self.client.patch('api/v2/interventions/5/',
        content_type='application/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 405)

    def test_edit_intervention_comment_empty(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(intervention))
        response = self.client.patch('api/v2/interventions/5/',
        content_type='application/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 405)

    def test_edit_redflag_status(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/10/status',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_redflag_status_exists(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/10/status',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_edit_intervention_status(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(intervention))
        response = self.client.patch('api/v2/interventions/7/status',
        content_type='application/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_delete_redflag(self):
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(self.incident))
        response = self.client.delete('api/v2/interventions/4',
        content_type='application/json',
        data=json.dumps(self.incident))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_delete_intervention(self):
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(self.incident))
        response = self.client.delete('api/v2/interventions/1',
        content_type='application/json',
        data=json.dumps(self.incident))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_only_creators_get_their_redflags(self):
        user_details = {
            "firstname": "test_firstn",
            "lastname": "test_lastname",
            "othernames": "test_othernames",
            "email": "not_admin1@email.com",
            "password": "1234555",
            "phoneNumber": "12345678",
            "username": "not admin1",
        }
        response = self.client.post('api/v2/auth/signup',
        data=json.dumps(user_details),
        content_type='application/json')
        token = json.loads(response.data.decode("utf-8"))
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(self.incident))
        response1 = self.client.get('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(self.incident))
        print(response1.data)
        self.assertEqual(response.status_code, 500)

    def test_only_creators_get_their_interventions(self):
        user_details = {
            "firstname": "test_firstn",
            "lastname": "test_lastname",
            "othernames": "test_othernames",
            "email": "not_admin@email.com",
            "password": "1234555",
            "phoneNumber": "12345678",
            "username": "not admin",
        }
        response = self.client.post('api/v2/auth/signup',
        data=json.dumps(user_details),
        content_type='application/json')
        token = json.loads(response.data.decode("utf-8"))
        self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(self.incident))
        response1 = self.client.get('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(self.incident))
        print(response1.data)
        self.assertEqual(response.status_code, 500)

    def test_redflag_comment_validation(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        response = self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_intervention_comment_validation(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        response = self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_intervention_comment_no_validation(self):
        redflag = {
            "id": "1",
            "location": "M",
            "status": "",
            "Images": "i, i",
            "Videos": "1, v",
            "type": "intervention"
        }
        response = self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_intervention_location_validation(self):
        intervention = {
            "id": "1",
            "comment": "test comment",
            "status": "draft",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        response = self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_intervention_no_location_validation(self):
        intervention = {
            "id": "1",
            "comment": "",
            "status": "draft",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        response = self.client.post('api/v2/interventions',
        content_type='application/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_redflag_location_validation(self):
        redflag = {
            "id": "1",
            "comment": "another one",
            "Images": "image1, image2",
            "status": "draft",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        response = self.client.patch('api/v2/redflags/10/location',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_intervention_status_validation(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention",
            "status": ""
        }
        response = self.client.patch('api/v2/interventions/7/status',
        content_type='application/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_can_only_edit_redflag_location(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        response = self.client.patch('api/v2/redflags/1/location',
        content_type='application/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_can_only_edit_intervention_location(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        response = self.client.patch('api/v2/interventions/1/location',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_can_only_edit_redflag_comment(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        response = self.client.patch('api/v2/redflags/3/comment',
        content_type='application/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_can_only_edit_intervention_comment(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "red-flag"
        }
        response = self.client.patch('api/v2/interventions/7/comment',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_can_only_edit_redflag_status(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(intervention))
        response = self.client.patch('api/v2/redflags/10',
        content_type='applicatiodata/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 405)

    def test_can_only_edit_redflag_status_empty(self):
        intervention = {
            "id": "1",
            "location": "Mukono",
            "status": "",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(intervention))
        response = self.client.patch('api/v2/redflags/10',
        content_type='applicatiodata/json',
        data=json.dumps(intervention))
        print(response.data)
        self.assertEqual(response.status_code, 405)

    def test_can_only_edit_intervention_status(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "draft",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/10/status',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)


    def test_can_only_edit_intervention_status_empty(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/10/status',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_can_only_edit_intervention_status_empty(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/10/status',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)


    def test_can_only_edit_intervention_comment_empty(self):
        redflag = {
            "id": "1",
            "location": "Mukono",
            "status": "here it is",
            "comment": "",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/10/status',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)


    def test_can_only_edit_intervention_location_empty(self):
        redflag = {
            "id": "1",
            "location": "",
            "status": "here we come",
            "comment": "another one",
            "Images": "image1, image2",
            "Videos": "video1, video2",
            "type": "intervention"
        }
        self.client.post('api/v2/redflags',
        content_type='application/json',
        data=json.dumps(redflag))
        response = self.client.patch('api/v2/redflags/10/status',
        content_type='application/json',
        data=json.dumps(redflag))
        print(response.data)
        self.assertEqual(response.status_code, 401)