
# Qiskit Fundamentals
# 1.3 H-Gate


from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# The H gate is a quantum gate that maps the |0⟩ state to the |+⟩ state and the |1⟩ state to the |−⟩ state.
# Thus it creates a superposition.

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()


print("H Gate Result:", counts)
plot_histogram(counts, title="H Gate on |0⟩")
plt.show()
