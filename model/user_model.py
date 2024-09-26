import mysql.connector
import json
class user_model():
    def __init__(self):
        # Connection establishment code
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="monumartinez", database="flask_api")
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Sucessfull")
        except:
            print("Database connection failure")
    def user_getall_model(self):
        # Business Logic
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if(len(result)>0):
            return json.dumps(result)
        else:
            return "No Data Found"