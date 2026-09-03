# Complexity Analysis — Sovereign Tensor Architecture

## Summary

| Layer | Time | Space | Qubits (basis) | Depth (est.) | Notes |
|-------|------|-------|----------------|--------------|-------|
| Classical dense GEMM | O(N³) | O(N²) | — | — | source |
| Online softmax | O(N²) | O(N) | — | — | source |
| Reversible GEMM | O(N³) | O(N²) + ancilla | — | — | Bennett |
| Quantum basis GEMM | poly | O(N²) qubits | high | high | no known asymptotic win for dense |
| Quantum amplitude | poly log | O(log N) | low | high | loading cost dominates |

**No quantum advantage is claimed for the dense attention workload without
additional structure.**

## Formal Invariants

- Shape preservation under Map / Scale
- Rank decrease exactly matches Contract / Reduce
- Microcode sequence length finite and terminates
- Reversible circuits return ancilla to |0⟩ (when claimed)
- Measurement distribution matches classical probability for encoded values
- Opcode encoding/decoding is bijective on the defined set
