from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def funcNDigitInt():

    dataGet = request.get_json(force=True)

    username = dataGet["username"]
    password = dataGet["password"]

    status = False

    with open("./db.json") as file:
        data = json.load(file)
        if username in data and password == data[username]:
            status = True
    
    dataReply = json.dumps( { "status": status } )
    return dataReply


