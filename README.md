
![image](https://user-images.githubusercontent.com/68393451/151698106-9d09631f-8883-4376-a01e-9ef92d1f317b.png)


# Q-Sup
A messaging interface using a QKD protocol

# Abstract

Here we propose an innovative way of secure key distribution using a web interface. Two users login to a server where they input a randomly generated number sequence with three digits. Depending on the input string, measurements are performed on an entangled state (Here, we use the anti-correlated bell state). For an N bit input, N bell-states are required. Then the users communicate their measurement labelings through a classical channel. They keep those particular measurement bits, for which the index of the input string is equal, and discard the remaining bits. Now the two users have inverted bit strings. One of the users flips their bit (also decided through the classical communication channel to get the secured key. This idea can be extended by using an n-qubit entangled state for n users. Our protocol is based on the E91 protocol.

# Theory

Our key distribution technique is based on the E91 protocol. 

![image](https://user-images.githubusercontent.com/68393451/151702199-7d0bac60-b2e0-405f-a7d0-5ac462314bba.png)

Image source: [link](https://medium.com/@qcgiitr/fundamentals-of-quantum-key-distribution-bb84-b92-e91-protocols-e1373b683ead)


# A little bit about Q - Sup
Q-Sup revolves around three parties : Alice, Bob and the server. Alice and Bob are assumed to be the users of the app nad the server is the intermediate channel.
Two users- A and B  and the server which serves as the intermediate channel. For two users to communicate, they need to input the same bit string. They need to excahnge this key in a way that is only known to them. 

The following flow chart encapsulates the working of the app :

![image](https://user-images.githubusercontent.com/68393451/151696305-77b7bbf9-b7fe-4c59-b434-88a15a4e9e81.png)






Set up -

```
pip install -r requirements.txt
python -m flask run
```

Resources -
<a href="https://www.freepik.com/vectors/background">Background vector created by coolvector - www.freepik.com</a>


