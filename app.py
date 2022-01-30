from flask import Flask, render_template, request
import json
app = Flask(__name__)

global_measurement_bases = {}

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

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

@app.route('/send_measurement_sequence', methods=['GET', 'POST'])
def send_measurement_sequence():

    dataGet = request.get_json(force=True)

    username = dataGet["username"]
    measurement_bases = dataGet["measurement-bases"]

    global_measurement_bases[username] = measurement_bases # Keeping the bases in a dict for now
    status = True

    print(global_measurement_bases)

    dataReply = json.dumps( { "status": status } )
    return dataReply


