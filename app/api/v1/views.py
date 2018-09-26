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
    post_data = request.get_json(force=True)

   
    if (not request.json or not "food_name" in request.json):
        return jsonify({'Error':"Request Not found"}), 400 #not found
    if request.json['food_name'] in [foodname['food_name'] for foodname in Ordered_items]:
      return jsonify({request.json['food_name']:"Aready Exist"}), 409 #conflict
  
    data={"id":len(Ordered_items)+1,
          "food_name":post_data.get('food_name'),
          "description":post_data.get('description'),
          "quantity":post_data.get('quantity'),
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


'''Fetch specific order'''
@app.route('/app/v1/orders/<int:order_id>',methods=['GET'])
def get_specific_order(order_id):
    order=[order for order in Ordered_items if order['id']==order_id]
    if not order:
        return jsonify({'Error':"Food Item Not Found"}), 404 #not found
    return jsonify({'food_item':order}), 200 #ok


'''Update the status of a specific order'''
@app.route('/app/v1/orders/<int:order_id>',methods=['PUT'])
def update_order_status(order_id):
    sent_data = request.get_json(force=True)
    data={"status":sent_data.get('status'),}
    if not request.json or not "status" in request.json:
       return jsonify({'Error':"Bad request"}), 400 
    order=[order for order in Ordered_items if order['id']==order_id]
    if not order:
        return jsonify({'Error':"Bad Request"}), 400
    order[0]["status"]=data["status"]
    return jsonify({'order':order}), 200 #ok

'''Delete specific order'''
@app.route('/app/v1/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    '''Delete a specific order'''
    for order in Ordered_items:
        if order['id'] == order_id:
            Ordered_items.remove(order)
            break
        else:
            return jsonify({'Error':'Not found'}) , 404 #bad request
    return jsonify({"Result": "Item Deleted Successfuly"}), 204
    
