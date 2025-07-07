
# Qiskit Fundamentals
# 1.9 CZ-Gate


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The CZ gate is a quantum gate that .
#      | 1 0 0  0 |
# CZ = | 0 1 0  0 |
#      | 0 0 1  0 |
#      | 0 0 0 -1 |

qc = QuantumCircuit(2, 2)

# Set control qubit to 1:
qc.x(0)

# Apply Hadamard gate to target qubit, putting it in superposition, |+⟩:
qc.h(1)

# Apply CZ with control=1, target=0, flips target to |-⟩:
qc.cz(0, 1)

# Apply Hadamard gate to target qubit, state becomes |1⟩:
qc.h(1)

qc.measure([0, 1], [0, 1])

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("CZ Result:", counts)
plot_histogram(counts, title="CZ Result of |10⟩")
plt.show()
