# app/api/v1/view.py

'''
This is where all API Endpoints will be captured
'''
from flask import jsonify,request
from app import app
from app.api.v1.models import Orders

Ordered_items=Orders().get_food_orders()

@app.route('/app/v1/orders', methods=['POST'])
def place_order():
    '''
    place a new order
    '''
    sent_data = request.get_json(force=True)
   
    if (not request.json or not "food_name" in request.json):
        return jsonify({'Error':"Request Not found"}), 400 #not found
    if request.json['food_name'] in [foodname['food_name'] for foodname in Ordered_items]:
      return jsonify({request.json['food_name']:"Aready Exist"}), 409 #conflict
  
    data={"id":len(Ordered_items)+1,
        "food_name":sent_data.get('food_name'),
        "description":sent_data.get('description'),
        "quantity":sent_data.get('quantity'),
        "status":'pending'}

    food_order={"id":data['id'],
                "food_name":data['food_name'],
                "description":data['description'],
                "quantity":data['quantity'],
                "status":'Not Confirmed'}

    Ordered_items.append(food_order)
    return jsonify({'Ordered_items':Ordered_items}), 201 #CREATED successfully


'''Get the list of all order'''
@app.route('/app/v1/orders',methods=['GET'])
def get_list_orders():    
    return jsonify({'Orders':Ordered_items}),200 #ok
