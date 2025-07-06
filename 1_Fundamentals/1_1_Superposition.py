
# Qiskit Fundamentals
# 1.1 Superposition


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# Create a single-qubit quantum circuit:
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to create a superposition state:
qc.h(0)

# Measure the qubit's state:
qc.measure(0, 0)

# Use the Aer simulator to execute the circuit:
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts(qc)


# Display measurements (should be evenly split):
print("Measurement results:", counts)
plot_histogram(counts)
plt.title("Superposition of a Qubit (H Gate)")
plt.show()
