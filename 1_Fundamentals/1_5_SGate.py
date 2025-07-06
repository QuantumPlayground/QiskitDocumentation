
# Qiskit Fundamentals
# 1.5 S-Gate


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The S gate is a quantum gate that rotates the phase of a qubit by π/4 radians.
# S = | 1 0 |
#     | 0 i |

qc = QuantumCircuit(1, 1)

# Start in |0⟩, H puts it in |+⟩:
qc.h(0)

# S rotates the phase of |+⟩, state becomes |i⟩:
qc.s(0)

# S again rotates the phase of |i⟩, state becomes |-⟩:
qc.s(0)

# Final H, outcome is |1⟩:
qc.h(0)

qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("S Gate Result:", counts)
plot_histogram(counts, title="S Gate on |+⟩")
plt.show()
