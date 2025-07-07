
# Qiskit Fundamentals
# 1.11 CCX


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The CCX (Toffoli) gate flips the state of a target qubit based on the state of two control qubits.
#       | 1 0 0 0 0 0 0 0 |
#       | 0 1 0 0 0 0 0 0 |
#       | 0 0 1 0 0 0 0 0 |
# CCX = | 0 0 0 1 0 0 0 0 |
#       | 0 0 0 0 1 0 0 0 |
#       | 0 0 0 0 0 1 0 0 |
#       | 0 0 0 0 0 0 0 1 |
#       | 0 0 0 0 0 0 1 0 |


qc = QuantumCircuit(3, 3)

# Set qubit 0 and 1 (controls) to |1⟩:
qc.x(0)
qc.x(1)

# Apply Toffoli (controls: 0,1 | target: 2):
qc.ccx(0, 1, 2)

qc.measure([0, 1, 2], [0, 1, 2])

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("CZ Result:", counts)
plot_histogram(counts, title="CZ Result of |10⟩")
plt.show()
