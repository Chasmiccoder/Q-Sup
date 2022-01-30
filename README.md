# Quantum-Maze
A Quantum Maze game that can be solved only with successful quantum key distribution.
Two users A and B are stuck in a maze and the only way they can leave the maze is by inputting the same bit of strings i.e. a secret key. However if anyone else learns their key that person will use the key to lock them in. 



# A little bit about the protocol in use : The E91 Quantum Key Distribution Protocol
 This QKD is primarily based on Quantum Entanglement. In other words, if two parties are entangled, then when a particular property is measured in one particle, instantaneously, the opposite state will be observed in the entangled state. It is impossible, however, to predict prior to measurement what state will be observed thus it is not possible to communicate via entangled particles without discussing the observations over a classical channel. So the basis of Ekert's protocol that we make use of in this project is the principle of communicating using entangled states aided by a classical information channel.

![image](https://user-images.githubusercontent.com/68393451/151692204-7eb03351-9baf-4d18-850f-2e0956ae4b63.png)

 The above image is a rough representation of the E91 protocol set-up

# A little bit about Q - Sup
Q-Sup revolves around three parties : Alice, Bob and the server. Alice and Bob are assumed to be the users of the app nad the server is the intermediate channel.

The following flow chart encapsultes the working of the app :

![image](https://user-images.githubusercontent.com/68393451/151696305-77b7bbf9-b7fe-4c59-b434-88a15a4e9e81.png)






Set up -

```
pip install -r requirements.txt
python -m flask run
```



