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
    def test_user_already_exist(self):
        '''
        Test API can create a new account (POST request)
        '''
        post_result=self.app.post('/app/v2/auth/signup',
                                 data=json.dumps(self.users),
                                 headers={'content_type':'application/json'})
        self.assertEqual(post_result.json,{'geoe@gmail.com': 'Aready Exist'})
        self.assertEqual(post_result.status_code,409)
    
    '''Test test create an account'''
    def test_user_create_account(self):
        response=self.app.post('/app/v2/auth/signup',
                                data=json.dumps(self.users),
                                headers={'content_type':'application/json'})
        self.assertEqual(response.json,{'message':'Account created successfuly'})
        self.assertEqual(response.status_code,201)
    
    '''Test Invalid email'''
    def test_invalid_email(self):
        response=self.app.post('app/v2/auth/signup',
                               data=json.dumps({"user_id":1,
                                                "username":'gege',
                                                "email":"geoegmail.com",
                                                "password":"g#2jd#D$4Bkl",
                                                "user_type":"user"}),
                               headers={'content_type':'application/json'})
        self.assertEqual(response.json,{'message': 'invalid Email'})
        self.assertEqual(response.status_code,401)

    '''Test Invalid password'''
    def test_invalid_password(self):
        response=self.app.post('app/v2/auth/signup',
                               data=json.dumps({"user_id":1,
                                                "username":'gege',
                                                "email":"geoe@gmail.com",
                                                "password":"g#fhb48",
                                                "user_type":"user"}),
                               headers={'content_type':'application/json'})
        self.assertEqual(response.json,{'message': 'invalid password'})
        self.assertEqual(response.status_code,401)
    
    def test_invalid_url(self):
        response=self.app.post('app/v2/auth/signiup',
                                data=json.dumps(self.users),
                                headers={'content_type':'application/json'})
        #self.assertEqual(response.json,{'message":"Request not found'})
        self.assertEqual(response.status_code,404)
    '''Test login'''
    def test_login(self):
        response=self.app.post('app/v2/auth/login',
                                data=json.dumps({"email":"geoe@gmail.com","password":"g#2jd#D$4Bkl"}),
                                headers={'content_type':'application/json'})
        self.assertEqual(response.json,{"message":"Login succesful"})


