from typing import List, Tuple, TypeVar


from typing import List


def even_odd(xs: List[int]) -> None:
    """
    Time: O(n), Space: O(1)

    Given a list of integers, reorder inplace so even entries appear first.

    Algorithm works by partitioning into 3 subarrays: Even, Odd, and Unclassified

    Everything starts as 'Unclassified', which we iterate through while moving boundaries of 'Even' and 'Odd' and shrinking 'Unclassified'.

    # >>> x = [1,2,3,4,5]; even_odd(x); print(x)
    # [4, 2, 3, 5, 1]
    #

    || Iteration 0  | Iteration 1   | Iteration 2   | Iteration 3   | Iteration 4   | Iteration 5   |
    -------------------------------------------------------------------------------------------------
    || Unclassified | [e1,2,3,4,o5] | [e5,2,3,o4,1] | [e4,2,o3,5,1] | [4,e2,o3,5,1] | [4,2,eo3,5,1] |
    || next_even    | 0             | 0             | 0++           | 1++           | 2             |
    || next_odd     | 4--           | 3--           | 2             | 2             | 2--           |

    """
    next_even: int = 0
    next_odd: int = len(xs) - 1

    while next_even < next_odd:
        if xs[next_even] % 2 == 0:
            next_even += 1
        else:
            xs[next_even], xs[next_odd] = (
                xs[next_odd],
                xs[next_even],
            )  # somehow this works as an in-place swap without needing a tmp value
            next_odd -= 1


# def even_odd_immutale(xs: List[int]) -> List[int]:
#     def helper(xs_: List[int]=xs, evens: Tuple[int, ...]=[], odds: Tuple[int, ...]=[]) -> Tuple[int, ...]:
#         match xs, evens, odds:
#             case [], _, _: return tuple(evens + odds)
#             case [x], _, _:
#                 if x % 2 == 0:
#                     return helper(xs)

# T = TypeVar('T')

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

# def quicksort_naive(xs: List[int]) -> List[int]:
#     pivot: int = len(xs) // 2

#     head = 0; last = 0

#     if xs[head] > xs[pivot]:    
#         if xs[last] < xs[pivot]:
#             xs[head], xs[last] = xs[last], xs[head]
#     if head < pivot:
#         if xs[head]
            
#         head += 1
#     if tail > pivot:
#         tail +=1

#     return []