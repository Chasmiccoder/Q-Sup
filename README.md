<p align="center">
  <img width="300" height="300" src="https://user-images.githubusercontent.com/68393451/151703663-3cf07b92-5ccb-4ab3-9335-e103a2943bc1.svg">
</p>


# Q-Sup
A web-based interface to perform QKD.

# Abstract

Here we propose an innovative way of secure key distribution using a web interface. Two users login to a server where they input a randomly generated number sequence with three digits. Depending on the input string, measurements are performed on an entangled state (Here, we use the anti-correlated bell state). For an N bit input, N bell-states are required. Then the users communicate their measurement labelings through a classical channel. They keep those particular measurement bits, for which the index of the input string is equal, and discard the remaining bits. Now the two users have inverted bit strings. One of the users flips their bit (also decided through the classical communication channel to get the secured key. This idea can be extended by using an n-qubit entangled state for n users. Our protocol is based on the E91 protocol.



# Walkthrough

1. User A logs in to the server.
2. The user then inputs a randomly generated string of three digits.
3. User B logs into server and does the same.
4. The two strings are sent to the backend to perform a sequence of measurements using a particular set of basis.
5. 

# Theory

Our key distribution technique is based on the E91 protocol with some slight changes. In our project we use a web-server as in intermediate interface which sends inputs to the QInspire backend and sends the measurement results to the respective user after performing partial measurements.

To learn more about the protocol go to this link: https://en.wikipedia.org/wiki/Quantum_key_distribution#E91_protocol:_Artur_Ekert_.281991.29

![image](https://user-images.githubusercontent.com/68393451/151702199-7d0bac60-b2e0-405f-a7d0-5ac462314bba.png)

Image source: [link](https://medium.com/@qcgiitr/fundamentals-of-quantum-key-distribution-bb84-b92-e91-protocols-e1373b683ead)







Set up -

```
pip install -r requirements.txt
python -m flask run
```

Resources -
<a href="https://www.freepik.com/vectors/background">Background vector created by coolvector - www.freepik.com</a>


