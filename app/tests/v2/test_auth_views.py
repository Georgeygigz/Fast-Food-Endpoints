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
                          "username":'george',
                          "email":"george@gmail.com",
                          "password":"g#2jdBkl",
                          "type":"user"}
    
    '''
    Test for placement of new order
    '''
    def test_create_new_account(self):
        '''
        Test API can place a new order (POST request)
        '''
        get_result=self.app.get('app/v1/orders',
                                 data=json.dumps(self.users),
                                 headers={'content_type':'application/json'})
        self.assertEqual(get_result.status_code,200)
        post_result = self.app.post('/app/v1/orders',data=json.dumps(self.users),
                                headers={'content_type':'application/json'})
        self.assertEqual(post_result.status_code, 409)