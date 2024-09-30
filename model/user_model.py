import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        # Database Connection establishment code
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="monumartinez", database="flask_api")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("Database Connection Sucessfull")
        except:
            print("Database connection failure")

    # GET ALL METHOD
    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if(len(result)>0):
            return make_response({"payload": result}, 200)
        else:
            return make_response({"Message": "No Data Found"}, 204)
    
    #GET BY ID
    def user_getbyid_model(self, id):
        try:
            query = "SELECT * FROM users WHERE id = %s"
            self.cur.execute(query, (id,))
            data = self.cur.fetchone()
            print(f"Query result: {data}")  # Debugging: Print the query result
            
            if data:
                return make_response({"Here's the result": data}, 200)
            else:
                return make_response({"Message": "No Data Found"}, 204)
        except Exception as e:
            return make_response({"Error": str(e)}, 500)


    # POST METHOD 
    def user_addone_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}') ")
        return make_response({"Message": "Profile Created Sucessfully.........."}, 201)
    
    # PUT METHOD
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']} ")
        if(self.cur.rowcount>0):
            self.cur.execute(f"SELECT * FROM users WHERE id={data['id']}")
            updated_data = self.cur.fetchone()  # Get the updated row
            print(f"Updated Data: {updated_data}")
            return make_response({"Message": "Profile Updated Sucessfully.........."}, 201)
        else:
            return make_response({"Message": "Nothing to update!!"}, 204)
        
    # PATCH METHOD    
    def user_patch_model(self, data, id):
        qry = "UPDATE users SET  "
        print("This is patch method")
        for key in data:
            qry = qry + f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id={id}"
        self.cur.execute(qry)
        if(self.cur.rowcount>0):
            return make_response({"Message": "Profile Updated Sucessfully.........."}, 201)
        else:
            return make_response({"Message": "Nothing to update!!"}, 204)
    
    # DELETE METHOD    
    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if(self.cur.rowcount>0):
            return make_response({"Message": "Profile Deleted Sucessfully.........."}, 200)
        else:
            return make_response({"Message": "This id doesn't Exists!!"}, 202)
        
