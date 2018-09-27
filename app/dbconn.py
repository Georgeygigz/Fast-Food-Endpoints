import psycopg2
import os

try:
	conn=psycopg2.connect("dbname='fastfood' user='postgres' host='localhost' port=5432 password='g@_gigz-2416'")
	curr=conn.cursor()

except Exception as e:
	print(e)


table_1="""CREATE TABLE IF NOT EXISTS users(
 	                   user_id INT ,
 	                   username VARCHAR UNIQUE NOT NULL,
 	                   email VARCHAR NOT NULL PRIMARY KEY,
 	                   password VARCHAR NOT NULL,
 	                   user_type VARCHAR NOT NULL);"""

                    
table_2="""CREATE TABLE IF NOT EXISTS orders(
                       orde_id INT,
 	                   food_id INT PRIMARY KEY,
 	                   food_name VARCHAR NOT NULL,
 	                   description VARCHAR NOT NULL,
 	                   quantity INT,
 	                   order_date Date,
 	                   status VARCHAR NOT NULL);"""

table_3="""CREATE TABLE IF NOT EXISTS meals(
 	                    meal_id INT ,
 	                    meal_name VARCHAR NOT NULL PRIMARY KEY,
 	                    price VARCHAR NOT NULL,
 	                    category VARCHAR UNIQUE NOT NULL,
 	                    description VARCHAR NOT NULL);"""

queries=[table_1,table_2,table_3]

