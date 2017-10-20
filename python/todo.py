from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

app.mongo = MongoClient("mongodb://mongo:27017", connect=False).tododb

@app.route("/todo.py")
def todo():
    items = app.mongo.tododb.find()
    return  render_template("todo.html", **locals())

@app.route("/todo.py/new")
def new():
 return render_template("todo.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
