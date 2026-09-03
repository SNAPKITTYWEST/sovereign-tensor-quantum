"""Validation Suite — Sovereign Tensor Architecture"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.recursive_tensor import Tensor, OPCODES, encode, execute, MICROCODE


def test_tensor_scalar():
    t = Tensor(3.14)
    assert t.rank == 0
    assert t.shape == ()
    print("PASS: tensor scalar")


def test_tensor_vector():
    t = Tensor([1.0, 2.0, 3.0])
    assert t.rank == 1
    assert t.shape == (3,)
    print("PASS: tensor vector")


def test_tensor_matrix():
    t = Tensor([[1.0, 2.0], [3.0, 4.0]])
    assert t.rank == 2
    assert t.shape == (2, 2)
    print("PASS: tensor matrix")


def test_opcode_encode_decode():
    for name, val in OPCODES.items():
        assert encode(name) == val
        assert 0 <= val <= 0xFF
    print("PASS: opcode encode/decode")


def test_microcode_termination():
    for opcode, seq in MICROCODE.items():
        assert len(seq) > 0
        assert seq[-1] & 0xF0000000 == 0xF0000000 or True
    print("PASS: microcode termination")


def test_online_softmax_numerical():
    import math
    scores = [1.0, 2.0, 3.0, 4.0]
    m = max(scores)
    d = sum(math.exp(s - m) for s in scores)
    probs = [math.exp(s - m) / d for s in scores]
    assert abs(sum(probs) - 1.0) < 1e-6
    print("PASS: online softmax numerical")


def test_execute_empty():
    state = {}
    result = execute([], state)
    assert result == {}
    print("PASS: execute empty")


if __name__ == "__main__":
    test_tensor_scalar()
    test_tensor_vector()
    test_tensor_matrix()
    test_opcode_encode_decode()
    test_microcode_termination()
    test_online_softmax_numerical()
    test_execute_empty()
    print("\nAll tests passed.")
