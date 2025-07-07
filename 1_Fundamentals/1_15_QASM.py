
# Qiskit Fundamentals
# 1.15 QASM


# QASM (Quantum Assembly Language) is a language for writing quantum circuits.
# Aer is a backend for simulating quantum circuits in QASM.

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.z(0)
qc.h(0)
qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("Measurement Result:", counts)
plot_histogram(counts, title="Simple Circuit Output")
plt.show()
