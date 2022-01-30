// document.getElementById('login-btn').onclick = function() {
//     let username = document.getElementById("username-inp").value;
//     let password = document.getElementById("password-inp").value;

//     authenticate(username, password);
// };




const authenticate = (event) => {
    event.preventDefault(); 

    let username = document.getElementById("username-inp").value;
    let password = document.getElementById("password-inp").value;
    var xml = new XMLHttpRequest();

    xml.open("POST", "/login", true);
    xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xml.onload = function() {
        var dataReply = JSON.parse(this.responseText);
        generatedNums = dataReply["numbers"];
        if (dataReply["status"] == false) {
            alert("Invalid username and password");
        } else {
            
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
    
    var div = document.getElementById("communicate-div");
    
    var form = document.createElement("form");
    form.setAttribute("id", "");

}




const login_form = document.getElementById("login-form");
login_form.onsubmit = authenticate;