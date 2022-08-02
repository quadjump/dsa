### 5.5 Delete duplicates from a sorted array ###

"""
This problem is concerned with deleting repeated elements from a sorted array. For example, for
the array (2,3,5,5,7,11,11,11,13), then after deletion, the array is (2,3,5,7,11,13,0,0,0). After
deleting repeated elements, there are 6 valid entries. There are no requirements as to the values
stored beyond the last valid element.

Write a program which takes as input a sorted array and updates it so that all duplicates have been
removed and the remaining elements have been shifted left to fill the emptied indices. Return the
number of valid elements. Many languages have library functions for performing this operation—
you cannot use these functions.

Hint: There is an O(n) time and O(1) space solution
"""

from typing import List, Optional


def dedup_sorted(xs: List[int], prev: Optional[int]=None) -> List[int]:
    """
    # >>> dedup_sorted([2,3,5,5,7,11,11,11,13])
    # [2, 3, 5, 7, 11, 13, 0, 0, 0]
    #
    """
    match xs, prev:
        case [], _: return []
        case [h], prev if h == prev: return []
        case [h], prev: return [h]
        case [h, *tail], prev:
            if h == prev:
                return dedup_sorted(tail, h) + [0]
            else:
                return [h] + dedup_sorted(tail, h)
        case _, _: raise Exception("Impossible bruh")


def dedup_in_place(xs: List[int]) -> List[int]:
    """
    # >>> dedup_sorted([2,3,5,5,7,11,11,11,13])
    # [2, 3, 5, 7, 11, 13, 0, 0, 0]
    #


    [2,3,5,13,7,11,11,11,5]
     f---^               b
    [2,3,5,7,13,11,11,11,5]
         p f          b
    [2,3,5,7,11,13,11,11,5]
         p f          b
    [2,3,5,7,13,11,11,11,5]
            p f          b
    [2,3,5,7,13,11,11,11,5]
            p f          b
    [2,3,5,7,13,11,11,11,5]
            p f          b  
    
    """
    match xs:
        case []: return []
        case [h]: return [h]
        case [h, t]: return [h] if h == t else [h, t]
        case _:
            front = 0; back = len(xs) - 1
            vacancy = front
            
            while front < back:
                if xs[front-1] == xs[front]:
                    xs[vacancy] = xs[front+1]
                    vacancy = front
                front += 1
            return []
                





