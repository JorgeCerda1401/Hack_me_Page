from flask import Flask, render_template, request, session, redirect, url_for
from data_base import Checker_User


app = Flask(__name__)

port = 80

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/home")
def home():
    if 'username' in session:
        return render_template("home.html")


@app.route("/process_form", methods=["POST"])
def process_form():
    input1 = request.form.get("input1")
    input2 = request.form.get("input2")
    
    # Do something with the input values, such as printing them
    flag = Checker_User(input1, input2)
    if flag:
        session['username'] = input1
        return redirect(url_for('home'))
    else:
        return "Username or password is not correct"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True ,port = port)