from app.api.v2.database import conn_db

# class FastFood():
#     def __init__(self):
#         pass
    

#     def save_users(self):
#         pass
    
#     def save_orders(self):
#         pass
    
#     def get_all_orders(self):
#         pass

#     def save_meals(self):
#         pass
    
#     def get_order_history(self):
#         pass 

class Users():
    def __init__(self,user_id=1,username="username",email="email",password="pass",user_type="user"):
        self.user_id=user_id
        self.username=username
        self.email=email
        self.password=password
        self.user_type=user_type
        self.db=conn_db()
    
    def create_new_user(self):
        database=self.db
        curr=database.cursor()
        query="INSERT INTO users (user_id, username,email, password,user_type) VALUES (%s,%s,%s,%s,%s);"
        curr.execute(query,(self.user_id,self.username,self.email,self.password,self.user_type))
        database.commit()
        return {"Message":"Data Save succefully"}, 201
    
    def get_all_users(self):
        conn=self.db
        curr=conn.cursor()
        query="""SELECT * FROM users;"""
        curr.execute(query)
        data=curr.fetchall()
        all_users=[]

        for k, v in enumerate(data):
            user_id, username, email, password, user_type=v
            users={"user_id": user_id, 
                    "username": username,
                    "email": email,
                    "password": password, 
                    "user_type": user_type}
            all_users.append(users)

        #curr.close()
        return all_users