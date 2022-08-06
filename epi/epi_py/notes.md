# Notes

- [Notes](#notes)
  - [Primitive Types](#primitive-types)
  - [Arrays](#arrays)
  - [Strings](#strings)
  - [Linked Lists](#linked-lists)

## Primitive Types
* Bitwise
  * `int.bitcount` for # of set bits (`pop_count` / Kernighan's algorithm)
  * `^` = XOR, `~` = NOT
  * Clear least set bit with `x & (x - 1)`
    * Ex. `0b11010 - (0b11010 - 1) = 0b11000`
  * Extract least set bit with `x & ~(x - 1)`
    * Ex. `0b11010 - ~(0b11010 - 1) = 0b10 = 2`
* Integers
  * `sys.maxsize` for max int (not really, just large #)

## Arrays

* Indexing
  * `x[-1]` retrieves back of list
  * `x[1:]` retrieves everything but head of list AKA the tail of the list
  * `x[-4:-1]`, `x[:]`, etc
* Swapping elements
  * `x[i], x[j] = x[j], x[i]` works (somehow?)
* Pattern Matching
  * 
    ```python
    match xs:
        # Structural matching on list
        case []: return...
        case [x]: return...
        case [x, *tail]: return...
        # Discarding values of matches
        case [x, *_]: return...
        case [_]: return...
        case _: return...
        # Guards
        case [_, *tail] if len(tail) ==...: return...
        case _ if xs[-1] > xs[0]: return...
    ```
* List methods
  * `list(range(100))` = [1..100]
  * `len`, `.append`, `.extend`, `.remove`, `.insert`
  * `del x[i]`
  * `.copy`
  * `.sort` vs `.sorted`
  * `.reverse` vs `.reversed`
  * `min`, `max`
  * `bisect`, `bisect_left`, `bisect_right` for insertion point in sorted list (from `bisect`)
  * `[x ** 2 for x in range(1,10) if x % 2 == 0]`
* FP Methods
  * `itertools`
    * `count`
    * `cycle`
    * `repeat(object, times)`
    * `groupby`
    * `takewhile`
    * `dropwhile`
    * `filter` / `filterfalse`
    * `tee`
    * `zip_longest`
    * `accumulate` - scan / a fold that returns intermediate accumulations
      * `accumulate([1,2,3,4,5], func=operator.add)` is `[1, 3, 6, 10, 15]`
  * `functools`
    * `reduce` (`functools.reduce(lambda x, acc: x + acc, range(10), 100` is `145`)
* EPI Tips
  * > Array problems often have simple brute-force solutions that use (9(h) space, but there are subtler solutions that use the array itself to reduce space complexity to 0(1).
  * > Filling an array from the front is slow, so see if it's possible to write values from the back.
  * > Instead of deleting an entry (which requires moving all entries to its left), consider overwriting it.
  * > When dealing with integers encoded by an array consider processing the digits from the back of the array. Alternately, reverse the array so the least-significant digit is the first entry.
  * > Be comfortable with writing code that operates on subarrays.
  * It's incredibly easy to make off-by-1 errors when operating on arrays—reading past the last element of an array is a common error which has catastrophic consequences.
  * > Don't worry about preserving the integrity of the array (sortedness, keeping equal entries together, etc.) until it is time to return.
  * > An array can serve as a good data structure when you know the distribution of the elements in advance. For example, a Boolean array of length W is a good choice for representing a subset of (0,1,..., W - 1}. (When using a Boolean array to represent a subset of {1,2,3,..., n], allocate an array of size n + 1 to simplify indexing.) .
  * > When operating on 2D arrays, use parallel logic for rows and for columns.
  * > Sometimes it's easier to simulate the specification, than to analytically solve for the result. For example, rather than writing a formula for the z-th entry in the spiral order for an n x n matrix, just compute the output from the beginning.

## Strings

* Immutable Representation
  * 
* String Methods
  * `.startswith`, `.endswith`
  * `.strip`
  * `.join`
  * `x[::-1]` to reverse string
* EPI Tips
  * > Similar to arrays, string problems often have simple brute-force solutions that use O(ri) space solution, but subtler solutions that use the string itself to reduce space complexity to (9(1).
  * > Understand the implications of a string type which is immutable, e.g., the need to allocate a new string when concatenating immutable strings. Know alternatives to immutable strings, e.g., a list in Python.
  * > Updating a mutable string from the front is slow, so see if it's possible to write values from the back.


## Linked Lists

```python
T = TypeVar('T')

@dataclass
class SingleyNode:
    data: T
    next_node: ListNode

@dataclass
class DoubleyNode:
    data: T
    next_node: DoubleyNode
    prev_node: DoubleyNode
```

* No pointers
  * Only cons lists, no doubly-linked lists
* `is` vs `==`
  * `is` checks for pointer equality AKA same object
* Unhashable Nodes
  * Custom data types are unhashable in python, so no building set or hashmap of nodes for checking cycles/overlaps unless gory conversion from Node -> tuple of data and pointer_location
* Fast and Slow pointer
  * Iterate with slow=slow.next and fast=fast.next.next to detect cycles with `if slow is fast`
* List Methods
    *
* EPI Tips
  * > List problems often have a simple brute-force solution that uses O(n) space, but a subtler solution that uses the existing list nodes to reduce space complexity to 0(1).
  * > Very often, a problem on lists is conceptually simple, and is more about cleanly coding what's specified, rather than designing an algorithm.
  * > Consider using a dummy head (sometimes referred to as a sentinel) to avoid having to check for empty lists. This simplifies code, and makes bugs less likely.
  * > It's easy to forget to update next (and previous for double linked list) for the head and tail.
  * > Algorithms operating on singly linked lists often benefit from using two iterators, one ahead of the other, or one advancing quicker than the other.