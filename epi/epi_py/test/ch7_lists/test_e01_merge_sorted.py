import sys
from typing import List
from hypothesis import given
import hypothesis.strategies as st

from ch7_lists.list_utils import Node, prepend, node_len
from ch7_lists.e01_merged_sorted import merge

rec_limit: int = sys.getrecursionlimit() // 2


@given(st.lists(st.integers(), max_size=rec_limit), st.lists(st.integers(), max_size=rec_limit))
def test_merge_length_(xs: List[int], ys: List[int]) -> None:
    xs_ = None; ys_ = None
    for x in xs: xs_ = prepend(x, xs_)
    for y in ys: ys_ = prepend(y, ys_)
    
    assert node_len(merge(xs_, ys_)) == node_len(xs_) + node_len(ys_)
