from flask import Flask
app = Flask(__name__)
# from controller import user_controller, product_controller
from controller import *

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "This is the Home Page!"


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)

