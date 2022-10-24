### 12.3 Implement an ISBN cache ###

"""
The International Standard Book Number (ISBN) is a unique commercial book identifier. It is a
string of length 10. The first 9 characters are digits; the last character is a check character. The check
character is the sum of the first 9 digits, mod 11, with 10 represented by 'X'. (Modem ISBNs use
13 digits, and the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs.)

Create a cache for looking up prices of books identified by their ISBN. You implement lookup,
insert, and remove methods. Use the Least Recently Used (LRU) policy for cache eviction. If an
ISBN is already present, insert should not change the price, but it should update that entry to be the
most recently used entry. Lookup should also update that entry to be the most recently used entry.

Hint: Amortize the cost of deletion. Alternatively, use an auxiliary data structure.
"""

from dataclasses import dataclass
from typing import Optional, OrderedDict


@dataclass
class ISBN_Cache:
    cache: OrderedDict[str, int]  # ISBN -> Price (int for simplicty)
    capacity: int = 1000


# def lru_evict(store: ISBN_Cache) -> ISBN_Cache:
#     """
#     # >>> x = ISBN_Cache(OrderedDict({"123X": 50, "456Y": 20})); lru_evict(x)
#     # ISBN_Cache(cache=OrderedDict([('123X', 50)]), capacity=1000)
#     #
#     """
#     store.cache.popitem()
#     return store


def lookup(isbn: str, store: ISBN_Cache) -> Optional[int]:
    """
    # >>> lookup("123X", ISBN_Cache(OrderedDict({"123X": 50, "456Y": 20})))
    # 50
    #
    """
    if isbn in store.cache:
        store.cache.move_to_end(isbn)
        return store.cache[isbn]
    return None


def insert(isbn: str, price: int, store: ISBN_Cache) -> ISBN_Cache:
    """
    # >>> store=ISBN_Cache(OrderedDict({"123X": 50, "456Y": 20}), 2); insert("789Z", 100, store)
    # ISBN_Cache(cache=OrderedDict([('456Y', 20), ('789Z', 100)]), capacity=2)
    #

    # >>> store=ISBN_Cache(OrderedDict({"123X": 50, "456Y": 20}), 2); lookup("123X", store); insert("789Z", 100, store)
    # 50
    # ISBN_Cache(cache=OrderedDict([('123X', 50), ('789Z', 100)]), capacity=2)
    """
    if len(store.cache) >= store.capacity:
        store.cache.popitem(last=False)
    store.cache.__setitem__(isbn, price)
    return store


def remove(isbn: str, store: ISBN_Cache) -> ISBN_Cache:
    """
    """
    store.cache.popitem(last=False)
    return store
