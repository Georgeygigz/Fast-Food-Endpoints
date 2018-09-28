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
    Test user can create new account
    '''
    def test_create_new_account(self):
        '''
        Test API can create a new account (POST request)
        '''
        post_result=self.app.post('/app/v2/auth/signup',
                                 data=json.dumps(self.users),
                                 headers={'content_type':'application/json'})
        self.assertEqual(post_result.status_code,201)
        post_result = self.app.post('/app/v2/auth/signup',data=json.dumps(self.users),
                                headers={'content_type':'application/json'})
        self.assertEqual(post_result.status_code, 409)
    

    '''Test user can login'''
    def test_user_login(self):
        response=self.app.post('/app/v2/auth/login',
                               data=json.dumps({'email':'georgey@gmail.com','password':'passs'}))
        self.assertEqual(response.status_code,200)