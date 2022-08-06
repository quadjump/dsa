import sys
from typing import List
from hypothesis import given
import hypothesis.strategies as st

from ch7_lists.list_utils import to_list, from_list

rec_limit: int = sys.getrecursionlimit() // 2


@given(st.lists(st.integers(), min_size=1, max_size=rec_limit))
def test_list_iso(xs: List[int]) -> None:
    assert xs == to_list(from_list(xs))
