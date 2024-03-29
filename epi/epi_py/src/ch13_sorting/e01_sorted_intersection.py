### 13.1 Compute the intersection of two sorted arrays ###

"""
A natural implementation for a search engine is to retrieve documents that match the set of words in
a query by maintaining an inverted index. Each page is assigned an integer identifier, its document-
ID. An inverted index is a mapping that takes a word w and returns a sorted array of page-ids which
contain w—the sort order could be, for example, the page rank in descending order. When a query
contains multiple words, the search engine finds the sorted array for each word and then computes
the intersection of these arrays—these are the pages containing all the words in the query. The most
computationally intensive step of doing this is finding the intersection of the sorted arrays.

Write a program which takes as input two sorted arrays, and returns a new array containing
elements that are present in both of the input arrays. The input arrays may have duplicate entries,
but the returned array should be free of duplicates. For example, the input is (2,3,3,5,5,6,7,7,8,12)
and (5,5,6,8,8,9,10,10), your output should be (5,6,8).

Hint: Solve the problem if the input array lengths differ by orders of magnitude. What if they are approximately
equal?
"""

from typing import List, TypeVar, Optional


T = TypeVar("T", bound=str | int)


def sorted_intersection(xs: List[T], ys: List[T]) -> List[T]:
    """
    # >>> sorted_intersection([2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10])
    # [5, 6, 8]
    #
    """
    return sorted(list(set(xs).intersection(set(ys))))

# TODO FIXME Unfinished
def sorted_intersection_(
    xs: List[T], ys: List[T], prev: Optional[T]
) -> List[T]:
    """
    # >>> sorted_intersection_([2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10])
    # [5, 6, 8]
    #
    """
    match xs, ys:
        case _, [] | [], _:
            return []
        case [x, *xtail], [y, *ytail]:
            if x == y:
                (
                    [x] if prev == None or x != prev else []
                ) + sorted_intersection_(xtail, ytail, x)
            elif x < y:  # type: ignore
                return sorted_intersection_(
                    xtail, ys, x if prev != None else None
                )
            else:
                return sorted_intersection_(
                    xs, ytail, y if prev != None else None
                )
