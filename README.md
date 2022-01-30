<p align="center">
  <img width="300" height="300" src="https://user-images.githubusercontent.com/68393451/151703663-3cf07b92-5ccb-4ab3-9335-e103a2943bc1.svg">
</p>


# Q-Sup
A messaging interface using a QKD protocol

# Abstract

Here we propose an innovative way of secure key distribution using a web interface. Two users login to a server where they input a randomly generated number sequence with three digits. Depending on the input string, measurements are performed on an entangled state (Here, we use the anti-correlated bell state). For an N bit input, N bell-states are required. Then the users communicate their measurement labelings through a classical channel. They keep those particular measurement bits, for which the index of the input string is equal, and discard the remaining bits. Now the two users have inverted bit strings. One of the users flips their bit (also decided through the classical communication channel to get the secured key. This idea can be extended by using an n-qubit entangled state for n users. Our protocol is based on the E91 protocol.

# Theory

Our key distribution technique is based on the E91 protocol. 

![image](https://user-images.githubusercontent.com/68393451/151702199-7d0bac60-b2e0-405f-a7d0-5ac462314bba.png)

Image source: [link](https://medium.com/@qcgiitr/fundamentals-of-quantum-key-distribution-bb84-b92-e91-protocols-e1373b683ead)


# Walkthrough

1. First User inputs a randomly generated string composed of 3 digits -1,2,3.
2. 

The following flow chart encapsulates the working of the app :

![image](https://user-images.githubusercontent.com/68393451/151696305-77b7bbf9-b7fe-4c59-b434-88a15a4e9e81.png)






Set up -

```
pip install -r requirements.txt
python -m flask run
```

Resources -
<a href="https://www.freepik.com/vectors/background">Background vector created by coolvector - www.freepik.com</a>


