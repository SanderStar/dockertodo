from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/todo.py")
def todo():
    return "<h1>TODO</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
