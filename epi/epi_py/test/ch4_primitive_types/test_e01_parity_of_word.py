from hypothesis import given, example
import hypothesis.strategies as st
from hypothesis.strategies import text

from ch4_primitive_types.e01_parity_of_word import *  # type: ignore


@given(st.integers(min_value=0, max_value=2**64))
def test_parity_popcount_mod2(word):
    assert bool(int.bit_count(word) % 2) == parity_popcount_mod2(word)


@given(st.integers(min_value=0, max_value=2**64))
def test_parity_brute(word):
    assert parity_popcount_mod2(word) == parity_brute(word)


@given(st.integers(min_value=0, max_value=2**64))
def test_parity_alt_popcount(word):
    assert parity_popcount_mod2(word) == parity_alt_popcount(word)
