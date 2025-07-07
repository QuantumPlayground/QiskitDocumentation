
# Qiskit Fundamentals
# 1.12 Measurement


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# In QC, states can be in superposition. After measurement, the state collapses probabilistically into a basis state.
# This collapse is irreversible (since information is lost), and the state becomes classical


# Create a circuit with an extra classical bit to record a second measurement:
qc = QuantumCircuit(1, 2)

# Put qubit in superposition:
qc.h(0)

# First measurement collapses it:
qc.measure(0, 0)

# Measure again into second classical bit:
qc.measure(0, 1)

# Simulate:
simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("Double Measurement (Collapse Demonstration):", counts)
plot_histogram(counts, title="Double Measurement: Collapse Confirmed")
plt.show()
