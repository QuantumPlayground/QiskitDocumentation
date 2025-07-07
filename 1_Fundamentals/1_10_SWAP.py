
# Qiskit Fundamentals
# 1.10 SWAP


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The SWAP gate exchanges the states of two qubits.
#        | 1 0 0 0 |
# SWAP = | 0 0 1 0 |
#        | 0 1 0 0 |
#        | 0 0 0 1 |

qc = QuantumCircuit(2, 2)

# Set qubit 0 to |1⟩, qubit 1 to |0⟩:
qc.x(0)

# Apply SWAP gate:
qc.swap(0, 1)

qc.measure([0, 1], [0, 1])

# NOTE: The result is |10⟩ since the order of the qubits is reversed (qubit 1 first, qubit 0 second).

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("CZ Result:", counts)
plot_histogram(counts, title="CZ Result of |10⟩")
plt.show()
