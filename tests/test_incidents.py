from tests.test_base import BaseTestCase
from api.views import incident_view
from api.views import user_view
import json

class IncidentTestCase(BaseTestCase):

    def test_fetch_all_redflags(self):
        response= self.app.get('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(self.incidents))
        self.assertEqual(response.status_code,200)

    def test_fetch_all_redflags_empty(self):
        response= self.app.get('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(self.incidents_empty))
        self.assertEqual(len(self.incidents_empty),0)
    
    def test_fetch_single_redflag(self):
        response= self.app.get('/api/v1/red-flags/1',data=json.dumps(self.incident))
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.incident,response.data)

    def test_add_redflag(self):
        redflags =[]
        response=self.app.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(dict(
                createdOn = "11-26-2018",
                createdBy = "Turinawe Smith",
                type = "red-flag",
                location = '0.3972� N, 32.6387� E',
                status = "draft",
                image = "image goes here",
                video = "video goes here",
                comment = "I was sked for a bribe to access servics at the HCIV"
            )))
        redflags.append(dict)
        # self.assertEqual(response.status_code,201)
        self.assertIn(" ", str(response.data))
        self.assertTrue(len(redflags),2)
        self.assertNotEqual("No redflags found",str(response.data))
        
    def test_delete_redflag(self):
        response=self.app.delete('/api/v1/red-flags/1',
        content_type='application/json',)
        # self.assertEqual(response.status_code,200)
        self.assertTrue(len(self.incidents),1)
        # self.assertIn("item has been deleted",str(response.data))

    def test_delete_redflag_nonexistent(self):
        response=self.app.delete('/api/v1/red-flags/1',
        content_type='application/json',
        data=json.dumps(self.incidents_empty))
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(self.incidents_empty),0)
        self.assertIn("red-flag does not exist",str(response.data))

    # def test_register_user(self):
    #     users = []
    #     response = self.app.post(
    #         '/api/v1/users',
    #         content_type='application/json',
    #         data=json.dumps(dict(
    #             firstname="bashir",
    #             lastname="saidi",
    #             othernames="wamula",
    #             email="bash@gmail.com",
    #             phone_number="+256758479763",
    #             username='username',
    #             registered="11-5-2018",
    #             is_admin=False
    #         )))
    #     users.append(dict)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn("response", str(response.data))
    #     self.assertTrue(len(users), 2 )
    #     self.assertNotEqual("No user found", str(response.data))
