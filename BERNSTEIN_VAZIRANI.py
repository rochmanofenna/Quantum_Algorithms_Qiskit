import qiskit
import qiskit_aer
import qiskit.visualization
import matplotlib
matplotlib.use('TkAgg')

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

def bernstein_vazirani(secret_string):
    n = len(secret_string)
    circuit = QuantumCircuit(n+1, n)

    circuit.x(n)
    circuit.h(n)

    for i in range(n):
        circuit.h(i)

    for i in range(n):
        if secret_string[i] == '1':
            circuit.cx(i, n)

    for i in range(n):
        circuit.h(i)

    for i in range(n):
        circuit.measure(i, i)

    return circuit

secret_string = '110'
bv_circuit = bernstein_vazirani(secret_string)
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(bv_circuit, shots=1024)
result = job.result()

counts = result.get_counts()
plot_histogram(counts).savefig('bv_result.png')

print("Result of the Bernstein-Vazirani algorithm (counts):", counts)
print("Plot saved as bv_result.png")
