from flask import Flask,render_template
import smtplib

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/home.html")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/men-products")
@app.route("/men.html")
def men_products():
    return render_template("men.html")

@app.route("/women-products")
@app.route("/women.html")
def women_products():
    return render_template("women.html")

@app.route("/kids-products")
@app.route("/kid.html")
def kid_products():
    return render_template("kid.html")

@app.route("/shopnow.html")
def buy():
    return render_template("shopnow.html")

@app.route("/confirmation.html")
def conform():
    return render_template("confirmation.html")

@app.route("/contactus.html")
def contact():
    return render_template("contactus.html")


if __name__ == "__main__":
    app.run(debug=True)