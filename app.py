from flask import Flask, render_template, request
import json
from quantum_backend import generateKey
app = Flask(__name__)

global_measurement_bases = {}
global_measurement_bases["received"] = 0
global_key = {}

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
    
    dataGet = request.get_json(force=True)  
    
    if len(global_key) == 0:
        global_key_tmp = generateKey(global_measurement_bases["user1"], global_measurement_bases["user2"])
        # global_key_tmp = ekert91(global_measurement_bases["user1"], global_measurement_bases["user2"])

        global_key["user1"] = global_key_tmp[0]
        global_key["user2"] = global_key_tmp[1]
    
    dataReply = json.dumps( { "key": global_key[dataGet["user"]] } ) # Send only the user's measurements. The user should not be able to view the other user's measurement
    
    print(global_key)
    return dataReply
