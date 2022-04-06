from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "Main Page <h1>Hello</h1>"

@app.route("/<name>")
def user(name):
    return "Hello "+name+"."

@app.route("/admin/admin")
def admin():
    return redirect(url_for("user", name="Admin"))


if __name__=="__main__":
    app.run()