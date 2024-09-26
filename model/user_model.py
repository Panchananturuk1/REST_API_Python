import mysql.connector
import json
class user_model():
    def __init__(self):
        # Database Connection establishment code
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="monumartinez", database="flask_api")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Sucessfull")
        except:
            print("Database connection failure")

    # GET METHOD
    def user_getall_model(self):
       
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if(len(result)>0):
            return json.dumps(result)
        else:
            return "No Data Found"

    # POST METHOD 
    def user_addone_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}') ")
        return "Profile Created Sucessfully.........."
    
    # PUT METHOD
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']} ")
        if(self.cur.rowcount>0):
            self.cur.execute(f"SELECT * FROM users WHERE id={data['id']}")
            updated_data = self.cur.fetchone()  # Get the updated row
            print(f"Updated Data: {updated_data}")
            return "Profile Updated Sucessfully.........."
        else:
            return "Nothing to update!!"
    # DELETE METHOD    
    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if(self.cur.rowcount>0):
            return "Profile Deleted Sucessfully.........."
        else:
            return "This id doesn't Exists!!"
