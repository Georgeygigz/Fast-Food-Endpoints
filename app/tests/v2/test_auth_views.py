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
                     "username":'geege',
                     "email":"geooe@gmail.com",
                     "password":"g#2jd#D$4Bkl",
                     "user_type":"user"}
    
    '''
    Test for placement of new order
    '''
    def test_existing_account(self):
        '''
        Test API can place a new order (POST request)
        '''
        post_result=self.app.post('/app/v2/auth/users',
                                  data=json.dumps(self.users),
                                  headers={'content_type':'application/json'})
        
        self.assertEqual(post_result.data,b'{\n  "geooe@gmail.com": "Aready Exist"\n}\n')
        self.assertEqual(post_result.status_code,409)
    
    def test_create_new_account(self):
        '''
        Test API can place a new order (POST request)
        '''
        post_result=self.app.post('/app/v2/auth/users',
                                  data=json.dumps(self.users),
                                  headers={'content_type':'application/json'})
        
        self.assertEqual(post_result.data,b'{\n  "message": "Account created successfuly"\n}\n')
        self.assertEqual(post_result.status_code,201)

    def test_invalid_email(self):
        '''
        Test for invalid url
        '''
        response=self.app.post('app/v2/auth/users',
                                data=json.dumps({"user_id":1,
                                                 "username":'geege',
                                                 "email":"geooemail.com",
                                                 "password":"g#2jd#D$4Bkl",
                                                 "user_type":"user"}),
                                headers={'content_type':'application/json'})
        self.assertEqual(response.data,b'{\n  "message": "invalid Email"\n}\n')
        self.assertEqual(response.status_code,401)
    
    def test_invalid_password(self):
        response=self.app.post('app/v2/auth/users',
                               data=json.dumps({"user_id":1,
                                                 "username":'geege',
                                                 "email":"geooemail@gmail.com",
                                                 "password":"gBkl",
                                                 "user_type":"user"}),
                              headers={'content_type':'application/json'})
        self.assertEqual(response.data, b'{\n  "message": "invalid password"\n}\n')
        self.assertEqual(response.status_code,401)

    def test_user_login(self):
        pass