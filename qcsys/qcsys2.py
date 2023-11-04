import time
import numpy as np
import pennylane as qml
import qutip as qt

# 10
dev = qml.device('default.qubit', wires=1, shots=4096)

@qml.qnode(dev)
def mach(theta): # mach-zehnder interferometer
    qml.Hadamard(wires=0) # hadamard the qubit
    qml.PhaseShift(theta, wires=0) # shift one branch
    qml.Hadamard(wires=0) # hadamard the qubit
    return qml.expval(qml.PauliZ(0)) # we end up with z

print(mach(np.pi / 2))
print(mach.draw().strip())

# 11
omega = 1
b = qt.Bloch()
def evolution_calc(tau):
    return np.array([[np.e ** ((-1j * omega * tau) / 2), 0], [0, np.e ** ((1j * omega * tau) / 2)]])

start = np.array([[1 / np.sqrt(2)], [1 / np.sqrt(2)]])
b.add_vectors([1 / np.sqrt(2), 1 / np.sqrt(2), 0])
for i in range(128):
    evolution = np.matmul(evolution_calc(i / 10), start)
    b.add_states(qt.Qobj(evolution), kind = "point")
b.show()

# 14
dev = qml.device('default.qubit', wires=2, shots=65536)

@qml.qnode(dev)
def sdc(bits):
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,1])
    if bits == "01":
    elif bits == "10":
    elif bits == "11":