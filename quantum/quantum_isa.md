# Quantum ISA — Sovereign Tensor Architecture

## Core Objects

- Logical qubits
- Classical bits (measurement results)
- Amplitude registers (for state-vector style)
- Basis-encoded tensors
- Ancilla pool

## Tensor Encoding Choices

1. **Amplitude encoding** (one tensor → one state vector) — exponential qubit cost
2. **Basis encoding** (each element a computational-basis state) — linear in size but requires more operations
3. **Hybrid block encoding**

## QIR Statement Examples

```
qreg q[8];
creg c[4];
tensor_encode %t0 into q[0:7] mode=basis;
rev_add q[0:3], q[4:7], anc[0:3];
measure q[0:3] → c[0:3];
```

## Quantum Opcodes

| Mnemonic | Meaning | Classical analogue |
|----------|---------|-------------------|
| QINIT | |0⟩ preparation | — |
| QX / QY / QZ | Pauli | — |
| QH | Hadamard | — |
| QCNOT | Controlled-NOT | — |
| QADD | Reversible add | TADD |
| QMUL | Reversible multiply (ancilla) | TMUL |
| QPERM | Permutation / shuffle | TSHFL |
| QMEAS | Measurement | — |
| QSYNC | Barrier | TSYNC |
| QANCILLA | Allocate / free ancilla | — |

No one-to-one mapping is assumed; each classical opcode is rewritten.
