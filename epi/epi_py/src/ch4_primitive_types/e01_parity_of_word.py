### Computing the Parity of a Word ###

"""
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For
example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
single bit errors in data storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.

How would you compute the parity of a very large number of 64-bit words?

Hint: Use a lookup table, but don't use 2^64 entries!
"""


def parity_popcount_mod2(word: int) -> bool:
    """
    `O(log b)` where `b` is the bitlength of input word

    Algorithm: "pop_count" to get number of set bits, then return 1 is if said count is odd, else 0

    Could be made a single log(b) pass by fusing pop_count and alternating parity flag.
    """
    return bool(word.bit_count() % 2)


def parity_brute(word: int) -> bool:
    """
    `O(b)` where `b` is the bitlength of input word

    Algorithm: "pop_count" to get number of set bits, then return 1 is if said count is odd, else 0
    """
    match word:
        case 0:
            return False
        case 1:
            return True

    if word & 1 == 1:
        return not (parity_brute(word >> 1))
    return parity_brute(word >> 1)


def parity_alt_popcount(word: int) -> bool:
    match word:
        case 0:
            return False
        case 1:
            return True
        case _:
            return not parity_alt_popcount(word & (word - 1))
