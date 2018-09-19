# app/models.py

'''This is the package that holds our database'''
class Orders():
    def __init__(self):
        self.food_orders=[]
    
    def get_food_orders(self):
        return self.food_orders
