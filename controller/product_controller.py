from app import app

@app.route("/user/product")
def product():
    return "This is product controller page"