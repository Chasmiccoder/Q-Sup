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
3. The server performs partial measurements on a sequence of entangled states and returns the result to the user.
4. User B logs in to the server and does the same.
5. The two users discuss their measurement sequence on a classical channel.
6. They retain the bits on those indices for which their measurements were performed on the same index.
7. One of the users inverts their bit string.

# Theory

Our key distribution technique is based on the E91 protocol. We propose to extend this idea to a greater number of users by using more qubits. For instance, if we want to secure a key among three users, we can use the ghz state. Depending on the initial state, some users may have to invert their strings to get the key.

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


