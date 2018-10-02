# app/api/v2/views.py

'''
This is where all API Endpoints will be captured
'''
import re
import datetime
import jwt
from functools import wraps
from passlib.hash import sha256_crypt
from flask import jsonify,request
from app import app
from app.api.v2.models import Users

all_user=Users().get_all_users()

'''create a token decorator function'''
def login_token_required(f):
    @wraps(f)
    def decorator_func(*args,**kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
        if not token:
            return jsonify({"message":"Please Login to continue"})
        try:
            data=jwt.decode(token,"secret")
            current_user=[c_user for c_user in all_user if c_user['user_id']==data['user_id']]
        except:
            return jsonify({"message":"Invalid token"}),401
        
        return f(current_user,*args, **kwargs)
    return decorator_func

'''Create a new account'''
@app.route('/app/v2/auth/users', methods=['POST'])
def create_account():
    '''
    Create a new user
    '''
    all_user=Users().get_all_users()

    sent_data = request.get_json(force=True)
   
    user_id=len(all_user)+1
    username= sent_data["username"]
    email= sent_data ["email"]
    password=sent_data["password"]
    user_type= "user"
    if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', request.json['email']):
            return jsonify({"message":"invalid Email"}),401

    if not re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])', request.json['password']):
        return jsonify({"message":"invalid password"}),401
    if request.json['email'] in [user['email'] for user in all_user]:
      return jsonify({request.json['email']:"Aready Exist"}), 409 #conflict
    if not request.json:
        return jsonify({"message":"Request not found"}),400
    
    new_user_detail={"user_id":user_id,
           "username":username,
           "email":email,
           "password":sha256_crypt.encrypt(password),
           "user_type":user_type}

    new_user=Users(**new_user_detail)
    new_user.create_new_user()
    return jsonify({"message":"Account created successfuly"}),201

'''Login endpoint'''
@app.route('/app/v2/auth/login',methods=['POST'])
def login():
    email=request.json['email']
    get_password=request.json['password']
    cur_user=[c_user for c_user in all_user if c_user['email']==email]

    if  len(cur_user) > 0:		
        password =cur_user[0]['password']
        if sha256_crypt.verify(get_password, password):
            exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
            token = jwt.encode({'user_id': cur_user[0]['user_id'], 'exp': exp_time},"secret")
            result={"message":"Login succesful, Welcome {}".format(cur_user[0]['username']), "token":token.decode('utf-8')}
            res=jsonify(result)
            
        else:
            return jsonify({"message":"Invalid Password"})
    else:
        return jsonify({"message":"Invalid Email"})

    return res
