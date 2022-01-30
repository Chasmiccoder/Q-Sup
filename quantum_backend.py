import os
import random
from apikey import token

from qiskit import execute
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit

from quantuminspire.credentials import enable_account, get_authentication
from quantuminspire.qiskit import QI

# Initiating the Quantum Inspire Account -
enable_account(token)
authentication = get_authentication()
QI.set_authentication()
qi_backend = QI.get_backend('QX single-node simulator')

def entangle_qubits(qc, q, q1, q2):
    """
    Puts the specified qubits in a maximally entangled state - |psi+>
    |psi+> = 1/root(2) * (|01> + |10>)
    
    Params:
    qc = quantum circuit object
    q  = qubits
    q1, q2 = the two qubits to be entangled
    """
    
    qc.h(q[q1])
    qc.x(q[q2])
    qc.cx(q[q1], q[q2])

def perform_measurement(qc, q, b, basis1, basis2):
    """
    Returns one bit of the key generated using the Ekert 91 protocol
    basis1 = Measurement basis of Alice
    basis2 = Measurement basis of Bob
    """
    
    alice = basis1
    bob = basis2

    if alice == 2:
        qc.x(q[0])

    if bob == 2:
        qc.x(q[1])

    qc.measure(q, b)
    qi_job = execute(qc, backend=qi_backend, shots=1)
    qi_result = qi_job.result()
    result = qi_result.get_counts(qc)

    outcome = list(result.keys())[0]
    return outcome[0], outcome[1]
    
def ekert91(basis1, basis2):
    
    q = QuantumRegister(2)
    b = ClassicalRegister(2)
    qc = QuantumCircuit(q, b)
    
    # Step 1 - Creating EPR Pair
    entangle_qubits(qc, q, 0, 1)
    
    # Step 2 - 
    outcome = perform_measurement(qc, q, b, basis1, basis2)
    return outcome[0], outcome[1]

def generateKey(bases1, bases2):
    if len(bases1) != len(bases2) or len(bases1) != 10:
        return False
    
    aliceOutcome = []
    bobOutcome = []
    
    # Taking 10 bits for our unsifted key
    n = 10
    for i in range(n):
        result = ekert91(bases1[i], bases2[i])
        aliceOutcome.append(int(result[0]))
        bobOutcome.append(int(result[1]))
    
    # Send the outcomes to the respective receivers
    # After this, Alice and Bob will publicly announce their measurement 
    # bases and obtain the sifted key!
    return aliceOutcome, bobOutcome

def generateBases(n):
    """
    Function to generate a psuedorandom sequence of bases 
    """
    bases = []
    
    for i in range(n):
        bases.append(random.randint(1,2))

    return bases

def getSiftedKey(key, user, bases1, bases2):
    siftedKey = []
    
    for i in range(len(bases1)):
        if bases1[i] == bases2[i]:
            if bases1[i] == 1: # Both measured along the Z basis, flip Bob's bit
                if user == "Bob":
                    if key[i] == 0:
                        siftedKey.append(1)
                    else:
                        siftedKey.append(0)
                else:
                    siftedKey.append(key[i])
            else: # Both measured along the X basis
                siftedKey.append(key[i])
    
    return siftedKey
