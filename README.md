<div align="center">

# sovereign-tensor-quantum

**Recursive Tensor-to-Quantum Architecture · ISA · Microcode · QIR · Reversible Transforms · Complexity Analysis**

[![License: Sovereign](https://img.shields.io/badge/License-Sovereign%20v1.0-blue.svg)](LICENSE)
[![License: BSL-1.1](https://img.shields.io/badge/License-BSL--1.1-green.svg)](LICENSE)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Language-Python-3776ab.svg)](src/)
[![Tests](https://img.shields.io/badge/Tests-7%20passing-brightgreen.svg)](tests/)

Full-stack formal specification: recursive tensor mathematics → Tensor IR → Classical ISA → Microcode → Classical Datapath → Reversible Layer → Quantum IR → Quantum Circuits.

</div>

---

## Architecture Stack

```mermaid
graph TB
    subgraph Layer1["Layer 1: Recursive Tensor Model"]
        T1[Tensor<br/>rank r, shape d₁…dᵣ]
        T2[Nested Tensor<br/>tree of tensors]
        T1 --> T2
    end
    subgraph Layer2["Layer 2: Tensor IR (TIR)"]
        IR1[Contract]
        IR2[Reduce]
        IR3[Map]
        IR4[Outer]
    end
    subgraph Layer3["Layer 3: Classical ISA"]
        ISA1[16 Opcodes<br/>TLOAD..THALT]
        ISA2[Microcode ROM<br/>32-bit words]
    end
    subgraph Layer4["Layer 4: Classical Datapath"]
        DP1[Multiplier Array]
        DP2[Reduction Network]
        DP3[Write-back]
    end
    subgraph Layer5["Layer 5: Reversible Layer"]
        RV1[Bennett Uncomputation]
        RV2[Ancilla Registers]
        RV3[Garbage Bits]
    end
    subgraph Layer6["Layer 6: Quantum IR + Circuits"]
        Q1[QIR Statements]
        Q2[Quantum ISA<br/>QINIT..QANCILLA]
        Q3[Circuit Output]
    end
    Layer1 --> Layer2
    Layer2 --> Layer3
    Layer3 --> Layer4
    Layer4 --> Layer5
    Layer5 --> Layer6
```

## Data Flow

```mermaid
graph LR
    MATH["Tensor Math<br/>definition 1.1"] --> TIR["Tensor IR<br/>type system"]
    TIR --> ISA["Classical ISA<br/>16 opcodes"]
    ISA --> MC["Microcode<br/>32-bit words"]
    MC --> HW["Datapath<br/>array + reduction"]
    HW --> REV["Reversible<br/>Bennett + ancilla"]
    REV --> QIR["Quantum IR<br/>QIR statements"]
    QIR --> QC["Quantum Circuits<br/>QX/QY/QZ/QH/QCNOT"]
```

## Primitive Operations

| Operation | Symbol | Rank Change | Reversible | Complexity |
|-----------|--------|-------------|------------|------------|
| Contract | ×ₖ | −2 | No* | O(∏d) |
| Reduce | red_f | −1 | No | O(∏d) |
| Map | map_f | 0 | Depends on f | O(∏d) |
| Outer | ⊗ | +ranks | Yes | O(∏d) |
| Add | + | 0 | Yes (ancilla) | O(∏d) |
| Scale | ·α | 0 | Yes | O(∏d) |

*Contraction is information-losing in the general case.

## Classical → Quantum Transformation

```mermaid
graph TD
    C_TADD["TADD Rd, Rs1, Rs2"] --> Q_TADD["QANCILLA anc<br/>QADD Rs1, Rs2, anc<br/>QPERM cleanup"]
    C_TMAX["TMAX Rd, Rs, dim"] --> Q_TMAX["Q̃ min-finding<br/>O(√N) queries<br/>or keep classical"]
    C_TCONTRACT["TCONTRACT"] --> Q_TCONTRACT["Block-encoding<br/>+ QSVT<br/>or classical tiling"]
```

## Complexity

| Layer | Time | Space | Qubits | Notes |
|-------|------|-------|--------|-------|
| Classical GEMM | O(N³) | O(N²) | — | Baseline |
| Online softmax | O(N²) | O(N) | — | Source-derived |
| Reversible GEMM | O(N³) | O(N²)+ancilla | — | Bennett |
| Quantum basis | poly | O(N²) qubits | high | No asymptotic win |
| Quantum amplitude | poly log | O(log N) | low | Loading cost dominates |

## File Structure

```
sovereign-tensor-quantum/
├── spec.md                    # Full recursive tensor model + TIR
├── complexity.md              # Complexity analysis + invariants
├── isa/
│   └── isa_spec.md            # 16-opcode classical ISA
├── quantum/
│   ├── quantum_isa.md         # QIR + quantum opcodes
│   └── transform_rules.md     # Classical → quantum rules
├── src/
│   └── recursive_tensor.py    # Reference implementation
└── tests/
    └── test_suite.py          # 7 tests (all passing)
```

## Run Tests

```bash
python tests/test_suite.py
# PASS: tensor scalar
# PASS: tensor vector
# PASS: tensor matrix
# PASS: opcode encode/decode
# PASS: microcode termination
# PASS: online softmax numerical
# PASS: execute empty
```

---

## Topics

`tensor-algebra` `quantum-computing` `ISA-design` `microcode` `reversible-computing` `QIR` `tensor-IR` `formal-spec` `GEMM` `attention` `Bennett-uncomputation` `quantum-circuits` `sovereign`

---

**Sovereign Source License v1.0 + BSL-1.1 + AGPL-3.0 (tri-license)**

Ahmad Ali Parr · Bel Esprit D'Accord Irrevocable Trust · EIN 42-697643
