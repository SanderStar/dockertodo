from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

app.mongo = MongoClient("mongodb://mongodb:27017", connect=False).tododb

@app.route("/todo.py")
def todo():
    items = app.mongo.tododb.find()
    return render_template("todo.html", items=items)

@app.route("/todo.py/new", methods=['POST'])
def newitem():
    name = request.form["name"]
    description = request.form["description"]
    # Toevoegen in database
    data = [{ "name": name, "description": description}]
    app.mongo.tododb.insert(data)
    return redirect("/todo.py")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
