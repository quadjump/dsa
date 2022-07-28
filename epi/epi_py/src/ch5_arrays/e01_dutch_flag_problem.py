### 5.1 The Dutch national flag problem ###

"""
The quicksort algorithm for sorting arrays proceeds recursively—it selects an element (the "pivot"),
reorders the array to make all the elements less than or equal to the pivot appear first, followed by
all the elements greater than the pivot. The two subarrays are then sorted recursively.

Implemented naively, quicksort has large run times and deep function call stacks on arrays with
many duplicates because the subarrays may differ greatly in size. One solution is to reorder the
array so that all elements less than the pivot appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot. This is known as Dutch national flag partitioning,
because the Dutch national flag consists of three horizontal bands, each in a different color.

As an example, assuming that black precedes white and white precedes gray. Figure 5.1(b) is a
valid partitioning for Figure 5.1(a). If gray precedes black and black precedes white. Figure 5.1(c)
is a valid partitioning for Figure 5.1(a).

Generalizing, suppose A = (0,1,2,0,2,1,1), and the pivot index is 3.
Then A[3] = 0, so (0,0,1,2,2,1,1) is a valid partitioning. For the same array, if the pivot index is 2, then A[2] = 2, so
the arrays (0,1,0,1,1,2,2) as well as (0,0,1,1,1,2,2) are valid partitionings.

Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[z] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.

Hint: Think about the partition step in quicksort.
"""

from typing import Callable, List, Tuple

def dutch_flag_partition_immutable(arr: List[int], pivot: int) -> List[int]:
    """
    All less than pivot first, followed by equal to pivot, and finally all greater than pivot at end.
    

    # >>> dutch_flag_partition_immutable([0,1,2,0,2,1,1], 3)
    # [0, 0, 1, 2, 2, 1, 1]
    #
    # >>> dutch_flag_partition_immutable([0,1,2,0,2,1,1], 4)
    # [0, 1, 0, 1, 1, 2, 2]
    #

    """
    match arr:
        case []: return []
        case [x]: return [x]
        case _:
            # Could fuse `split . filter` for single pass 
            lesser: List[int] = list(filter(lambda x: x < arr[pivot], arr)) # O(n) time/space
            same: List[int] = list(filter(lambda x: x == arr[pivot], arr)) # O(n) time/space
            greater: List[int] = list(filter(lambda x: x > arr[pivot], arr)) # O(n) time/space
            
            return lesser + same + greater  # Log(n) executions (time) + Log(qs calls) call stack (space)
        

def quicksort_immutable(arr: List[int]) -> List[int]:
    match arr:
        case []: return []
        case [x]: return [x]
        case [head, *tail]:
            # Could fuse `split . filter` for single pass 
            lesser: List[int] = list(filter(lambda x: x < head, tail)) # O(n) time/space
            greater: List[int] = list(filter(lambda x: x >= head, tail)) # O(n) time/space
            
            return quicksort_immutable(lesser) + [head] + quicksort_immutable(greater)  # Log(n) executions (time) + Log(qs calls) call stack (space)
        case _: raise Exception("Shouldn't happen, pinky promise. Python can't do exhaustiveness checking lmao")


def quicksort(arr: List[int]) -> None:
    return quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr: List[int], left: int, right: int) -> None:
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort_helper(arr, left, partition_pos - 1)
        quicksort_helper(arr, partition_pos + 1, right)


def partition(arr: List[int], left: int, right: int) -> int:
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i
