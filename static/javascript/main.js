const authenticate = (event) => {
    event.preventDefault(); 

    let username = document.getElementById("username-inp").value;
    let password = document.getElementById("password-inp").value;
    var xml = new XMLHttpRequest();

    xml.open("POST", "/login", true);
    xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xml.onload = function() {
        var dataReply = JSON.parse(this.responseText);
        
        if (dataReply["status"] == false) {
            alert("Invalid username and password");
        } else {
            currentUser = username;
            initiateTextChannel();
        }
    };

    dataSend = {
        "username" : username,
        "password" : password
    };
    
    xml.send(JSON.stringify(dataSend));
}

const initiateTextChannel = () => {
    var loginDiv = document.getElementById("login-div");
    loginDiv.style.display = 'none'; // hide

    // A short write up of how this works
    str = "The Measurement possibilities are as follows. For user 1 - A1, A2, A2. For user 2 - B1, B2, B3";
    str += "A1 = Alice measures along the Z Basis, A2 = Alice measures along the X Basis, A3 - Alice measures along the 1/root(2) * (Z + X) basis";
    str += "B1 = Bob measures along the Z Basis, B2 = Bob measures along the 1/root(2) * (Z - X) basis, B3 - Bob measures along the 1/root(2) * (Z + X) basis";

    var description = document.createElement("p");
    description.setAttribute("id", "description-p");
    description.setAttribute("value", str);
    
    var div = document.getElementById("communicate-div");
    
    var form = document.createElement("form");
    form.setAttribute("id", "send-measurement");
    
    var measurementSequence = document.createElement("input");
    measurementSequence.setAttribute("type", "text");
    measurementSequence.setAttribute("name", "measurement-sequence");
    measurementSequence.setAttribute("placeholder", "enter measurement bases");
    measurementSequence.setAttribute("id", "measurement-bases-inp");

    // submit the bases to interface
    var sub = document.createElement("input");
    sub.setAttribute("type", "submit");
    sub.setAttribute("value", "Submit");

    
    var sendStatus = document.createElement("p");
    sendStatus.setAttribute("id", "send-status-p");  

    form.appendChild(measurementSequence);
    form.appendChild(sub);
    div.appendChild(description);
    div.appendChild(form);
    div.appendChild(sendStatus);
    
    const measurement_form = document.getElementById("send-measurement");
    measurement_form.onsubmit = sendMeasurement;
}

// function to send the user's measurement bases sequence to the intermediate interface
const sendMeasurement = (event) => {
    event.preventDefault();

    document.getElementById("send-status-p").innerHTML = "Sending measurement bases...";
    

    let stringSequence = document.getElementById("measurement-bases-inp").value;

    let bases = [];

    if(stringSequence.length != 10) {
        alert("Please insert exactly 10 measurement bases"); // quick hack, since this is a prototype
        return;
    }
    
    for(let i = 0; i < stringSequence.length; i++) {
        let element = stringSequence[i];
        if(isNumber(element) && parseInt(element) >= 1 && parseInt(element) <= 3) {
            bases.push(parseInt(element));
        } else {
            alert("Invalid Input!");
            return;
        }
    }

    console.log(bases);
    
    var xml = new XMLHttpRequest();

    xml.open("POST", "/send_measurement_sequence", true);
    xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xml.onload = function() {
        var dataReply = JSON.parse(this.responseText);
        // measurement_results = dataReply["result"]; // string with the entire, unsifted key
        console.log("reply", dataReply);
        if(dataReply["status"]) {
            document.getElementById("send-status-p").innerHTML = "Your bases have been sent the interface successfully!";
        } else {
            document.getElementById("send-status-p").innerHTML = "Oops, something went wrong. Please try again :(";
        }
    };

    dataSend = {
        "username": currentUser,
        "measurement-bases" : bases
    };
    
    xml.send(JSON.stringify(dataSend));
}

const isNumber = (str) => {
    if(typeof str != "string") {
        return false;
    } else {
        return !isNaN(str) && !isNaN(parseFloat(str));
    }
}


var currentUser = null;

const login_form = document.getElementById("login-form");
login_form.onsubmit = authenticate;


