from app import app
from model.user_model import user_model
from flask import request
obj = user_model()

# GET ALL METHOD
@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

# GET BY ID
@app.route("/user/<id>", methods=["GET"])
def user_getbyid_controller(id):
    return obj.user_getbyid_model(id)

# POST METHOD 
@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

# PUT METHOD
@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)

# PATCH METHOD
@app.route("/user/patch/<id>", methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)

# DELETE METHOD
@app.route("/user/delete/<id>", methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)
