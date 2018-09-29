import psycopg2
import os
from app.dbconn import queries



def conn_db():
	try:
		conn=psycopg2.connect("dbname='fastfood' user='postgres' host='localhost' port=5432 password='g@_gigz-2416'")
	except Exception as e:
		raise e
	return conn

def create_table():
	conn=conn_db()
	curr=conn.cursor()
	try:
		for query in queries:
			curr.execute(query)
		conn.commit()
	except Exception as e:
		print(e)


def destory():
	conn =conn_db()
	curr=conn.cursor()
	orders="DROP TABLE IF EXISTS  orders CASCADE"
	meals="DROP TABLE IF EXISTS  meals CASCADE"
	users="DROP TABLE IF EXISTS  users CASCADE"
	drop_queries=[orders,meals,users]
	try:
		for query in drop_queries:
			curr.execute(query)
		conn.commit()
	except Exception as e:
		print(e)


