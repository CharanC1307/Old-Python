from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("Flask2.1.html")

@app.route("/hello")
def cool():
    return render_template("Flask2.2.html")

@app.route("/<name>/<age>")
def user1(name, age):
    return render_template("Flask2.3.html", Name=name, Age=age, charan=2)

@app.route("/<name>")
def user2(name):
    return render_template("Flask2.4.html", Name=name)

@app.route("/list")
def user3():
    return render_template("Flask2.5.html", list=["Charan", "Sharvin", "Deepa", "Chandran"])


if __name__=="__main__":
    app.run()