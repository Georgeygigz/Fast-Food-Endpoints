#app/tests/test_models.py
'''Test case for our data storage'''

import unittest
from app.api.v1.models import Orders

class TestModelCases(unittest.TestCase):
    '''TestFoodOrders class  and methods'''

    def setUp(self):
        '''Set up the model.'''
        self.food_items = Orders()
    
    '''Test for available data'''
    def test_available_records(self):
        '''The model intialized with some records'''
        self.assertEqual(self.food_items.get_food_orders(),[])

if __name__ == "__main__":
    unittest.main()