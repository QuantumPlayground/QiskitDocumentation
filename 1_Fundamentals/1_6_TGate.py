
# Qiskit Fundamentals
# 1.6 T-Gate


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The T gate is a quantum gate that rotates the phase of a qubit by π/8 radians.
# T = | 1     0   |
#     | 0  e^iπ/4 |

qc = QuantumCircuit(1, 1)

# Start in |0⟩, H puts it in |+⟩:
qc.h(0)

# T applied 4 times rotates the phase of |+⟩, state becomes |-⟩:
qc.t(0)
qc.t(0)
qc.t(0)
qc.t(0)

# Final H, outcome is |1⟩:
qc.h(0)

qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("T Gate Result:", counts)
plot_histogram(counts, title="T Gate on |+⟩")
plt.show()
