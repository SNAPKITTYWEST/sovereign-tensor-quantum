# Classical → Quantum Transformation Rules

## Irreversible Operations Identified

- Reduction (max, sum)
- Contraction (general case)
- Overflowing arithmetic
- Destructive stores

## Reversible Techniques

- Bennett-style uncomputation
- Ancilla registers for intermediate results
- Garbage bits for lost information
- Reversible arithmetic (e.g., controlled-add, modular operations)

## State Tuple

(data, ancilla, garbage)

Uncomputation restores ancilla to |0…0⟩ when possible.

## Example: Vector Add

Classical: `TADD Rd, Rs1, Rs2`
Reversible: controlled-add with ancilla

```
QANCILLA anc
QADD Rs1, Rs2, anc
QPERM … (cleanup)
```

## Example: Reduction (max)

Generally irreversible.

Quantum options:
- Approximate via quantum minimum-finding (Dürr–Høyer) — query complexity O(√N)
- Or keep classical and only quantize surrounding linear algebra

## Contract / GEMM

Block-encoding + Quantum Singular Value Transformation or classical tiling
kept and only local reversible arithmetic quantised.

Full quantum speedup requires sparse or low-rank structure not present in
dense GEMM.
