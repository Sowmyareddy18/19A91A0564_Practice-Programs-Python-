#step1
import sqlite3

#step2
con=sqlite3.connect('F:\\cseAA.db')
print("connection object is created successfully")

#step3-create cursor Object-cursor() method is available with Connection object
cursorObj = con.cursor()
print("Cursor Object created successfully")
#step4-Execute queries-execute()---on cursor
cursorObj.execute("CREATE table movies(name text, rating integer)")
print("Movie Table Created succssfully")
'''
connection object is created successfully
Cursor Object created successfully
Movie Table Created succssfully
'''
