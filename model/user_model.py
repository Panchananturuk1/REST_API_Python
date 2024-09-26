import mysql.connector
import json
class user_model():
    def __init__(self):
        # Connection establishment code
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="monumartinez", database="flask_api")
            self.con.autocommit=True
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
        
    def user_addone_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}') ")
        return "Profile Created Sucessfully.........."
    
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']} ")
        if(self.cur.rowcount>0):
            return "Profile Updated.........."
        else:
            return "Nothing to update!!"
