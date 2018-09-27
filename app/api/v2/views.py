# app/api/v2/view.py

'''
This is where all API Endpoints will be captured
'''
import re
from passlib.hash import sha256_crypt
from flask import jsonify,request
from app import app
from app.api.v2.models import Users


    

@app.route('/app/v2/users', methods=['POST'])
def create_account():
    '''
    Create a new user
    '''
    all_user=Users().get_all_users()

    sent_data = request.get_json(force=True)
   
    user_id=len(all_user)+1
    username= sent_data["username"]
    email= sent_data ["email"]
    password= sent_data["password"]
    user_type= "user"
    


    new_user_detail={"user_id":user_id,
           "username":username,
           "email":email,
           "password":password,
           "user_type":user_type}

    new_user=Users(**new_user_detail)
    new_user.create_new_user()
    return jsonify({"message":"Account created successfuly"})
