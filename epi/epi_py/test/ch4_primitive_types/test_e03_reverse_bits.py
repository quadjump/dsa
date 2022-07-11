from hypothesis import given, example
import hypothesis.strategies as st
from hypothesis.strategies import text

from ch4_primitive_types.e02_swap_bits import swap_bits, is_set_at  # type: ignore
from ch4_primitive_types.e03_reverse_bits import reverse_bits, reverse_bits_brute, reverse_bits_recursive  # type: ignore


@given(st.integers(min_value=0, max_value=2**64))
def test_reverse_bits(word: int) -> None:
    # assert reverse_bits_brute(word) == reverse_bits_recursive(word)
    # assert reverse_bits_brute(word) == reverse_bits(word)
    assert reverse_bits(word) == reverse_bits_recursive(word)
    # reverse_bits(word)


def test_unit_reverse_bits() -> None:
    assert reverse_bits(0b0) == 0b0
    assert reverse_bits(0b1) == 0b1
    assert reverse_bits(0b10) == 0b1
    assert reverse_bits(0b001) == 0b1
    assert reverse_bits(0b100) == 0b1
    assert reverse_bits(0b101) == 0b101
    assert reverse_bits(0b110) == 0b011
    assert reverse_bits(0b111) == 0b111


def test_unit_reverse_bits_recursive() -> None:
    assert reverse_bits_recursive(0b0) == 0b0
    assert reverse_bits_recursive(0b1) == 0b1
    assert reverse_bits_recursive(0b10) == 0b01
    assert reverse_bits_recursive(0b001) == 0b1  # msb_pos=0
    assert reverse_bits_recursive(0b100) == 0b1
    assert reverse_bits_recursive(0b101) == 0b101
    assert reverse_bits_recursive(0b110) == 0b011
    assert reverse_bits_recursive(0b111) == 0b111


def test_unit_reverse_bits_brute() -> None:
    assert reverse_bits_brute(0b0) == 0b0
    assert reverse_bits_brute(0b1) == 0b1
    assert reverse_bits_brute(0b10) == 0b1
    assert reverse_bits_brute(0b001) == 0b1
    assert reverse_bits_brute(0b100) == 0b1
    assert reverse_bits_brute(0b101) == 0b101
    assert reverse_bits_brute(0b110) == 0b011
    assert reverse_bits_brute(0b111) == 0b111
