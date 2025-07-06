
# Qiskit Fundamentals
# 1.8 CNOT-Gate


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The CNOT (Controlled NOT) gate is a quantum gate that flips the state of a qubit based on the state of another qubit.
#        | 1 0 0 0 |
# CNOT = | 0 1 0 0 |
#        | 0 0 0 1 |
#        | 0 0 1 0 |

qc = QuantumCircuit(2, 2)

# Set control qubit to 1:
qc.x(0)

# Apply CNOT with control=1, target=0, flips target to 1:
qc.cx(0, 1)

qc.measure([0, 1], [0, 1])

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("CNOT Result:", counts)
plot_histogram(counts, title="CNOT Result of |10⟩")
plt.show()
