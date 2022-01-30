from flask import Flask, render_template, request
import json
from quantum_backend import generateKey
app = Flask(__name__)

global_measurement_bases = {}
global_measurement_bases["received"] = 0

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
    global_measurement_bases["received"] += 1
    status = True

    print(global_measurement_bases)

    dataReply = json.dumps( { "status": status } )
    return dataReply

@app.route('/check_handshake', methods=['GET', 'POST'])
def check_handshake():
    status = False

    users = global_measurement_bases.keys()
    if "user1" in users and "user2" in users:
        status = True
    
    dataReply = json.dumps( { "status": status } )
    return dataReply

@app.route('/perform_quantum_key_distribution', methods=['GET', 'POST'])
def perform_quantum_key_distribution():
    key = generateKey(global_measurement_bases["user1"], global_measurement_bases["user2"])
    dataReply = json.dumps( { "key": key } )
    return dataReply
