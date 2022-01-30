
![image](https://user-images.githubusercontent.com/68393451/151698106-9d09631f-8883-4376-a01e-9ef92d1f317b.png)


# A little bit about the protocol in use : The E91 Quantum Key Distribution Protocol
 This QKD is primarily based on Quantum Entanglement. In other words, if two parties are entangled, then when a particular property is measured in one particle, instantaneously, the opposite state will be observed in the entangled state. It is impossible, however, to predict prior to measurement what state will be observed thus it is not possible to communicate via entangled particles without discussing the observations over a classical channel. So the basis of Ekert's protocol that we make use of in this project is the principle of communicating using entangled states aided by a classical information channel.

![image](https://user-images.githubusercontent.com/68393451/151692204-7eb03351-9baf-4d18-850f-2e0956ae4b63.png)

 The above image is a rough representation of the E91 protocol set-up

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



