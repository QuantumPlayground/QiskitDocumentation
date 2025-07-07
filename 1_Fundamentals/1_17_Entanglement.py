
# Qiskit Fundamentals
# 1.17 Entanglement


from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(1)

# The two qubits in this first circuit are not entangled, just independent qubits.

state = Statevector.from_instruction(qc)
print("Two-Qubit Product State (|0+⟩):\n", state)

# The two qubits in this second circuit are entangled, you cannot describe one independently.

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

state = Statevector.from_instruction(qc)
print("Bell State (|00⟩ + |11⟩):\n", state)
