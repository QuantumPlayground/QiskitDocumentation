
# Qiskit Fundamentals
# 1.2 X-Gate


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The X (Pauli) gate is a quantum gate that flips the state of a qubit (x-axis rotation).
# X = | 0 1 |
#     | 1 0 |

qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("X Gate Result:", counts)
plot_histogram(counts, title="X Gate on |0⟩")
plt.show()
