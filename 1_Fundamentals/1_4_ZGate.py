
# Qiskit Fundamentals
# 1.4 Z-Gate


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The Z (Pauli) gate is a quantum gate that flips the phase of a qubit.
# Z = | 1 0  |
#     | 0 -1 |

qc = QuantumCircuit(1, 1)

# Start in |0⟩, H puts it in |+⟩:
qc.h(0)

# Z flips phase of |1⟩, state becomes |-⟩:
qc.z(0)

# Final H, outcome is |1⟩:
qc.h(0)

qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("Z Gate Result:", counts)
plot_histogram(counts, title="Z Gate on |0⟩")
plt.show()
