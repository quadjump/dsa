from hypothesis import given, example
import hypothesis.strategies as st
from hypothesis.strategies import text

from ch4_primitive_types.e02_swap_bits import swap_bits, is_set_at  # type: ignore


@given(
    st.integers(min_value=0, max_value=2**64),
    st.integers(min_value=0, max_value=63),
    st.integers(min_value=0, max_value=63),
)
@example(16, 0, 1)
def test_swap_bits(word: int, i: int, j: int) -> None:
    swapped = swap_bits(word, i, j)
    
    assert word |is_set_at| i == swapped |is_set_at| j
    assert word |is_set_at| j == swapped |is_set_at| i
