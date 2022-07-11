### Reverse Bits ###

"""
Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer con­
sisting of the bits of the input in reverse order. For example, if the input is (1110000000000001), the
output should be (1000000000000111).

Hint: Use a lookup table.
"""

import math

from ch4_primitive_types.e02_swap_bits import swap_bits  # type: ignore


def reverse_bits(word: int) -> int:
    """
    O(log b) where b is length of bits

    # >>> bin(reverse_bits(0b1110000000000001))
    # '0b1000000000000000'
    #
    # >>> bin(reverse_bits(0b11101))
    # '0b10111'
    #
    # >>> bin(reverse_bits(0b01))
    # '0b1'
    #

    Algorithm:
    * Find maximum set bit to use as boundary.
    * Perform O(log b) pop_count-esque traversal of set bits
        * Per iteration, extract least set bit and accumulate reversed set bits on result (lsb -> msb - lsb)
    """
    if word == 0:
        return 0

    msb_pos = msb(word)
    res = 0
    lsb_pos = 0

    while word != 0:
        lsb_pos = int(
            math.log2(word & ~(word - 1))
        )  # least set bit extraction trick
        res |= 2 ** (msb_pos - lsb_pos)  # accumulate set bits in reverse order

        word = word & (word - 1)  # traverse set bits

    return res


def reverse_bits_recursive(word: int) -> int:
    """
    O(log b) where b is length of bits

    # >>> bin(reverse_bits_recursive(0b1110000000000001))
    # '0b1000000000000111'
    #

    # >>> bin(reverse_bits(0b11101))
    # '0b10111'
    #
    # >>> bin(reverse_bits_recursive(0b10))
    # '0b1'
    #

    Algorithm:
    * Find maximum set bit to use as boundary.
    * Perform O(log b) pop_count-esque traversal of set bits
        * Per iteration, extract least set bit and accumulate reversed set bits on result (lsb -> msb - lsb)
    """
    match word:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            # Maximum set bit remains same for life of algorithm as lower bits are cleared first
            msb_pos: int = msb(word)
            # Least set bit extraction trick
            lsb_pos: int = int(math.log2(word & ~(word - 1)))
            # Accumulate rotated set bits while only traversing set bits
            return int(2 ** (msb_pos - lsb_pos)) | reverse_bits_recursive(
                word=word & (word - 1)
            )


def msb(word: int, max_pos: int = 64) -> int:
    """
    O(log b) where b is set

    # >>> msb(0b1110000000000001)
    # 15
    #
    # >>> msb(0b101)
    # 2
    #

    `pop_count`-esque with extracting instead of clearing lsb until lsb-pos > maxpos
    """
    if word <= 1:
        return 0
    msb_pos = 0
    while word != 0 and msb_pos < 2**max_pos:
        msb_pos = word & ~(word - 1)
        word = word & (word - 1)
    return int(math.log2(msb_pos))


def reverse_bits_brute(word: int) -> int:
    """
    O(b) where b is length of bitstring

    # >>> bin(reverse_bits_brute(0b1110000000000001))
    # '0b1000000000000111'
    #

    # >>> bin(reverse_bits_brute(0b10))
    # '0b1'
    #
    """
    msb_pos = msb(word)
    for x in range(0, msb_pos):
        word = swap_bits(word, x, msb_pos - x)
        if x >= msb_pos // 2:
            break
    return word
