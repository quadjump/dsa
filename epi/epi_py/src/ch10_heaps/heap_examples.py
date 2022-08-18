import heapq
import itertools
from typing import List, Tuple


def top_k(k: int, stream: List[str]) -> List[str]:
    """
    Given a "streaming" sequence of strings, compute the `k` longest strings

    # >>> top_k(3, ["abc", "efg", "hi", "jklm"])
    # ['efg', 'efg', 'jklm']
    #
    # >>> k=3; stream=["abc", "efg", "hi", "jklm"]; [(len(s), s) for s in itertools.islice(stream, k)]
    # [(3, 'abc'), (3, 'efg'), (2, 'hi')]
    #
    """
    # Entries are compared by their lengths
    min_heap: List[Tuple[int, str]] = [
        (len(s), s) for s in itertools.islice(stream, k)
    ]
    heapq.heapify(min_heap)

    for next_string in stream:
        # Push next_string and pop the shortest in min_heap
        heapq.heappushpop(min_heap, (len(next_string), next_string))

    return [p[1] for p in heapq.nsmallest(k, min_heap)]

### Neetcode Heap - Kth Largest element - Leetcode 703 ###

num_stream: List[int] = [10, 9, 8, 7, 6, 5, 4, 3, 99, 1]
kth_pos: int = 3

def kth_largest(k: int, nums: List[int]) -> int:
    """
    Mutates input stream into heap

    Given a "streaming" sequence of strings, compute the `k` longest strings

    # >>> kth_largest(3, [10, 9, 8, 7, 6, 5, 4, 3, 99, 1])
    # 9
    #
    # >>> k=3; nums=[10, 9, 8, 7, 6, 5, 4, 3, 99, 1]; kth_largest(k, nums); nums
    # 9
    # [99, 10, 5, 8, 9, 1, 4, 3, 7, 6]
    #
    """
    heapq._heapify_max(nums)
    res = [heapq._heappop_max(nums) for _ in range(k)]
    nums += res
    heapq._heapify_max(nums)
    return res[-1]


def add(val: int) -> int:
    """
    # >>> [print((add(x), num_stream)) for x in [12,14,1,98,2,104]]
    # (10, [99, 12, 8, 7, 10, 5, 4, 1, 3, 6, 9])
    # (12, [99, 14, 12, 7, 10, 8, 4, 1, 3, 6, 9, 5])
    # (12, [99, 10, 14, 7, 9, 12, 4, 1, 3, 1, 6, 5, 8])
    # (14, [99, 10, 98, 7, 9, 12, 14, 1, 3, 1, 6, 5, 8, 4])
    # (14, [99, 10, 98, 7, 9, 8, 14, 1, 3, 1, 6, 2, 5, 4, 12])
    # (98, [104, 98, 99, 10, 9, 8, 14, 7, 3, 1, 6, 2, 5, 4, 12, 1])
    # [None, None, None, None, None, None]
    #
    """
    num_stream.append(val)
    return kth_largest(kth_pos, num_stream)