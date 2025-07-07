
# Qiskit Fundamentals
# 1.14 Quantum Circuits


from qiskit import QuantumCircuit

# Build a simple 1-qubit circuit:
qc = QuantumCircuit(1, 1)

# Apply quantum gates:
qc.h(0)
qc.z(0)
qc.h(0)

# Measure:
qc.measure(0, 0)

# Draw the circuit:
print(qc)
