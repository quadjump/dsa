from hypothesis import given, example
import hypothesis.strategies as st
from hypothesis.strategies import text

from ch5_arrays.e03_mult_arb_precision import fromDigitList, multiply_, sum_, toDigitList

@given(st.integers(min_value=-9999, max_value=9999), st.integers(min_value=-9999, max_value=9999))
def test_multiply_(n: int, m: int) -> None:
    assert toDigitList(n * m) == multiply_(toDigitList(n), toDigitList(m))


@given(st.integers(min_value=-9999, max_value=9999), st.integers(min_value=-9999, max_value=9999))
def test_sum_(n: int, m: int) -> None:
    assert toDigitList(n + m) == sum_(toDigitList(n), toDigitList(m))
