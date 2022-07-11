### Swap Bits ###

"""
There are a number of ways in which bit manipulations can be accelerated. For example, as described on Page 23,
the expression x & (x-1) clears the lowest set bit in x, and x & ~(x-1) extracts the lowest set bit of x.

Here are a few examples: 
* 16 &  (16 - 1) = 0
* 11 &  (11 - 1) = 10
* 20 &  (20 - 1) = 16
* 16 & ~(16 - 1) = 16
* 11 & ~(11 - 1) = 1
* 20 & ~(20 - 1) = 4

###############################################################
#### Figure 4.1: Example of swapping a pair of bits. ##########

0 1 0 0 1 0 0 1
^MSB          ^LSB

(a) The 8-bit integer 73 can be viewed as array of bits,
with the LSB being at index 0.


0 0 0 0 1 0 1 1
^MSB          ^LSB

(b) The result of swapping the bits at indices 1 and 6, with
the LSB being at index 0. The corresponding integer is 11.
###############################################################

A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the
least significant bit (LSB), and the bit at index 63 corresponding to the most significant bit (MSB).
Implement code that takes as input a 64-bit integer and swaps the bits at indices i and j. Figure 4.1
illustrates bit swapping for an 8-bit integer.

Hint: When is the swap necessary?
"""

from utils import Infix


def swap_bits(word: int, i: int, j: int) -> int:
    """
    O(1).

    # >>> bin(37)
    # '0b100101'
    #
    # >>> bin(swap_bits(37, 0, 0))
    # '0b100101'
    #
    # >>> bin(swap_bits(37, 1, 0))
    # '0b100110'
    #
    # >>> bin(swap_bits(37, 4, 2))
    # '0b110001'
    #
    # >>> bin(swap_bits(37, 2, 4))
    # '0b110001'
    #


    Algorithm:
    * Check whether i-th and j-th bits are set
    * If both or neither, then no change needed
    * Otherwise, flip both i-th and j-th bits regardless via bitmask `xor` word (ex. i=7,j=3, mask=0b00i000j00)
    """
    match word | is_set_at | i, word | is_set_at | j:
        case True, True:
            return word
        case False, False:
            return word
        case _:
            # Flip both i and j bits, regardless of settedness
            ij_mask = 2**i | 2**j
            return int(ij_mask ^ word)


@Infix
def is_set_at(word: int, x: int) -> bool:
    """
    O(1).

    Checks if bit at x-pos is set
    """
    return int(word & (2**x)) != 0
