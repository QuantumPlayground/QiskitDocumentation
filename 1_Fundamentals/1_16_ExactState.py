
# Qiskit Fundamentals
# 1.16 Exact State


# Using Statevector, we can get the exact state of a quantum circuit:

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc_sv = QuantumCircuit(1)
qc_sv.h(0)
qc_sv.z(0)
qc_sv.h(0)

# Get the statevector:
state = Statevector.from_instruction(qc_sv)
print("Final statevector:", state)
