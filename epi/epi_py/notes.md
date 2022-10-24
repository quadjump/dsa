# Notes

- [Notes](#notes)
  - [Primitive Types](#primitive-types)
  - [Arrays](#arrays)
  - [Strings](#strings)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
    - [Queues](#queues)
  - [Heaps](#heaps)
  - [Search](#search)
  - [Hashing](#hashing)
  - [Sorting](#sorting)

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

[Back to Top⤴](notes.md#notes)

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

[Back to Top⤴](notes.md#notes)

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

[Back to Top⤴](notes.md#notes)

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

[Back to Top⤴](notes.md#notes)

## Stacks

* Stacks vs Queues
  * Stacks = LIFO (stack on and take from top, ex. stacking and removing boxes)
  * Queues = FIFO (queueing up element, ex. given bunch of orders, serve oldest first)
* Stack API
  * `push`: cons O(1)
    * In python, lambda x, xs: [x] + xs)
    * Amortized O(1) for dynamically-resizing array
  * `pop`: head O(1) (`pop()`)
  * `peek`: xs[0] (look at head but don't remove) O(1)
* Via `collections.deque` (when lists aren't enough)
  * > Generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
  * Methods
    *  `append` (snoc)
    * `appendleft` (cons)
    * `clear`
    * `count`
    * `extend`
    * `index(x, ...)` (search)
    * `insert(ix, x)`
    * `pop`
    * `popleft`
    * `remove`
    * `reverse`
    * `rotate`
* Via regular lists `[]`
    * `.append(e)`
    * `xs[-1]`
    * `.pop()`
    * define empty as `len(xs) == None`
* Via `import queue` 
  * Queue Types
    * `Queue(maxsize=0)`
    * `LifoQueue(maxsize=0)` (AKA a stack)
    * `PriorityQueue(maxsize=0)`
    * `SimpleQueue`
  * Methods
    * `qsize()` Queue -> int
    * `empty` Queue -> bool
    * `full` Queue -> bool
    * `put(item,...)` Queue[T] -> T -> Queue[T]
    * `get()` Queue[T] -> T 
* EPI Tips
  * > Learn to recognize when the stack LIFO property is applicable. For example, parsing typically benefits from a stack.
  * > Consider augmenting the basic stack or queue data structure to support additional operations, such as finding the maximum element.


[Back to Top⤴](notes.md#notes)

### Queues

* Methods
  * `.append(e)`
  * `q[0]` = head
  * `q[-1]` = last
  * `q.popleft()` = tail (aka remove head)


[Back to Top⤴](notes.md#notes)

## Heaps

[`heapq` in base libray](https://docs.python.org/3/library/heapq.html#module-heapq)

[Back to Top⤴](notes.md#notes)

## Search

[Back to Top⤴](notes.md#notes)

## Hashing

[Back to Top⤴](notes.md#notes)

## Sorting

* Sorting Methods
  * `sort(key: Optional[x -> x], reverse: bool)`
    * in-place sorting
  * `sorted()`
    * returns new sorted sequence
* EPI Tips
  * Sorting problems come in two flavors: (1.) use sorting to make subsequent steps in an algo­rithm simpler, and (2.) design a custom sorting routine. For the former, it's fine to use a librarysort function, possibly with a custom comparator. For the latter, use a data structure like a BST, heap, or array indexed by values.
  * Certain problems become easier to understand, as well as solve, when the input is sorted. The most natural reason to sort is if the inputs have a natural ordering, and sorting can be used as a preprocessing step to speed up searching.
  * For specialized input, e.g., a very small range of values, or a small number of values, it's possible to sort in 0(n) time rather than 0(n log n) time.
  * It's often the case that sorting can be implemented in less space than required by a brute-force approach.
  * Sometimes it is not obvious what to sort on, e.g., should a collection of intervals be sorted on starting points or endpoints? (Problem 13.5 on Page 186)

[Back to Top⤴](notes.md#notes)
[Back to Top⤴](notes.md#notes)
[Back to Top⤴](notes.md#notes)
[Back to Top⤴](notes.md#notes)
[Back to Top⤴](notes.md#notes)
[Back to Top⤴](notes.md#notes)

