from flask import Flask, render_template, request
from data_base import Checker_User
from waitress import serve


app = Flask(__name__)

port = 80

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/process_form", methods=["POST"])
def process_form():
    input1 = request.form.get("input1")
    input2 = request.form.get("input2")
    
    # Do something with the input values, such as printing them
    flag = Checker_User(input1, input2)
    if flag:
        
        return home()
    else:
        return "Username or password is not correct"


if __name__ == "__main__":
    serve(app, host="0.0.0.0" ,port = port)