# app/test/v1/test_views.py

'''
Testing our api endpoints
'''

import unittest
import json
from app import app
from app.api.v1.models import Orders

food_orders=Orders().get_food_orders()


class TestApiEndpoint(unittest.TestCase):
    def setUp(self):
        '''
        Code executed before every test
        '''
        self.app = app.test_client()
        self.app.testing = True
        self.food_items ={"id":1,
                          "food_name":'Piza',
                          "description":"fast",
                          "quantity":2,
                          "status":"pedding"}
    
    '''
    Test for placement of new order
    '''
    def test_user_can_place_an_order(self):
        '''
        Test API can place a new order (POST request)
        '''
        get_result=self.app.get('app/v1/orders',
                                 data=json.dumps(self.food_items),
                                 headers={'content_type':'application/json'})
        self.assertEqual(get_result.status_code,200)
        post_result = self.app.post('/app/v1/orders',data=json.dumps(self.food_items),
                                headers={'content_type':'application/json'})
        self.assertEqual(post_result.status_code, 409)


    '''Test for getting the list of order'''
    def test_get_list_of_orders(self):
        '''Test API Endpoint can get list of order(GET Request)'''
        response=self.app.get('/app/v1/orders',
                              headers={'content_type': 'application/json'})        
        self.assertEqual(response.status_code, 200)

    
    '''Test fetch for specific order'''
    def test_fetch_specific_order(self):
        '''Test fetch for specific order API endpoint [GET request]'''
        response =self.app.post('/app/v1/orders',
                                    data=json.dumps(self.food_items),
                                    headers={'content_type': 'application/json'})

        self.assertEqual(response.status_code,201)
        
        result=self.app.get('/app/v1/orders/1',
                            headers={'content_type': 'application/json'})
        self.assertEqual(result.status_code,200)
