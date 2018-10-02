# app/test/v2/test_views.py

'''
Testing our api endpoints
'''

import unittest
import json
from app import app

class TestApiEndpoints(unittest.TestCase):
    def setUp(self):
        '''
        Code executed before every test
        '''
        self.app = app.test_client()
        self.app.testing = True
        self.users ={"user_id":1,
                     "username":'gege',
                     "email":"geoe@gmail.com",
                     "password":"g#2jd#D$4Bkl",
                     "user_type":"user"}
    
    '''
    Test for placement of new order
    '''
    def test_create_new_account(self):
        '''
        Test API can place a new order (POST request)
        '''
        post_result=self.app.post('/app/v2/auth/users',
                                 data=json.dumps(self.users),
                                 headers={'content_type':'application/json'})
        result=json.loads(post_result.data.decode())
        self.assertEqual(post_result.json["message"],"Account created successfuly")
        self.assertEqual(post_result.status_code,201)

        post_result = self.app.post('/app/v2/users',data=json.dumps(self.users),
                                headers={'content_type':'application/json'})
        self.assertEqual(post_result.status_code, 409)

    def test_user_login(self):
        pass