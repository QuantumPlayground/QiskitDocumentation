
# Qiskit Fundamentals
# 1.7 Y-Gate


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The Y (Pauli) gate is a quantum gate that flips the phase as well as the state of a qubit (y-axis rotation).
# T = | 0 -i |
#     | i  0 |

qc = QuantumCircuit(1, 1)

# Start in |0⟩, H puts it in |+⟩:
qc.h(0)

# Y flips phase and state of |+⟩, state becomes |-⟩:
qc.y(0)

# Final H, outcome is |1⟩:
qc.h(0)

qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("Y Gate Result:", counts)
plot_histogram(counts, title="Y Gate on |+⟩")
plt.show()
