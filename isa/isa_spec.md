# Custom ISA (Classical) — Sovereign Tensor Architecture
# Minimal opcode set (4-bit base + extensions)

## Opcodes

| Opcode | Mnemonic | Encoding | Operands | Latency | Reversible |
|--------|----------|----------|----------|---------|------------|
| 0000 | NOP | 0x00 | — | 1 | itself |
| 0001 | TLOAD | 0x10+reg | Rd, addr | 5–20 | TLOAD† |
| 0010 | TSTORE | 0x20+reg | Rs, addr | 5–20 | TSTORE† |
| 0011 | TADD | 0x30 | Rd, Rs1, Rs2 | 2 | TADD (ancilla) |
| 0100 | TMUL | 0x40 | Rd, Rs1, Rs2 | 3 | TMUL (ancilla) |
| 0101 | TCONTRACT | 0x50 | Rd, Rs1, Rs2, dims | 10–100 | none (lossy) |
| 0110 | TREDUCE | 0x60+op | Rd, Rs, dim, op | 5–30 | none (lossy) |
| 0111 | TMAP | 0x70+f | Rd, Rs, f | 2–8 | depends on f |
| 1000 | TSCALE | 0x80 | Rd, Rs, imm | 2 | TSCALE |
| 1001 | TMAX | 0x90 | Rd, Rs, dim | 5–15 | none |
| 1010 | TEXP | 0xA0 | Rd, Rs | 4–10 | approx. |
| 1011 | TSHFL | 0xB0 | Rd, Rs, mode | 2 | TSHFL |
| 1100 | TSYNC | 0xC0 | — | 1–5 | itself |
| 1101 | TCMOV | 0xD0 | Rd, Rs, pred | 1 | TCMOV |
| 1110 | TBARRIER | 0xE0 | — | variable | itself |
| 1111 | THALT | 0xF0 | — | 1 | itself |

† Requires copy-out ancilla for true reversibility.

## Source Mapping

- mma.sync → TCONTRACT + TMUL sequence
- cp.async → TLOAD with async flag (extension bit)
- online softmax → TMAX + TEXP + TREDUCE + TSCALE loop

## Microinstruction Word (32-bit)

```
[31:28] seq_ctrl
[27:24] reg_we
[23:20] alu_op
[19:16] mem_ctrl
[15:12] tensor_ctrl
[11:8]  reduce_ctrl
[7:4]   branch_ctrl
[3:0]   special
```

## Microcode Sequence (TCONTRACT example)

```
0x1000_0001 ; enable left feeder
0x1000_0010 ; enable right feeder
0x1100_0001 ; fire multiplier array
0x1100_0010 ; accumulate
0x1010_0001 ; optional max reduction
0x0010_0001 ; write-back
0x1111_0000 ; end sequence
```

ISA opcode → decoder ROM → microinstruction sequence → datapath control signals → state transition.
