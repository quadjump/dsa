### Find a closest integer with the same weight ###

"""
Define the weight of a nonnegative integer x to be the number of bits that are set to 1 in its binary
representation. For example, since 92 in base-2 equals (1011100)_2, the weight of 92 is 4.

Write a program which takes as input a nonnegative integer x and returns a number y which is not
equal to x, but has the same weight as x and their difference, \y - x|, is as small as possible. You can
assume x is not 0, or all 1s. For example, if x - 6, you should return 5. You can assume the integer
fits in 64 bits.
"""

# Weight of bitstring = pop_count(bitstring)

import math
from ch4_primitive_types.e02_swap_bits import swap_bits  # type: ignore


def closest_same_weight_integer(word: int) -> int:
    """
    # >>> closest_same_weight_integer(0b1) == 0b10
    # True
    #

    This algorithm computes with left preference (as opposed to 0b101 which would also work).
    # >>> closest_same_weight_integer(0b101) == 0b110

    Closeness as in |input word - output word| ~= 0

    Algorithm:
    * Run short-circuiting pop_count with extraction until curr_lsb > prev_lsb << 1
        * Per iteration, record `curr_lsb` and update `prev_lsb`
    * Swap between prev_lsb position and (prev_lsb + 1) position
    """
    if word == 0:
        return 0
    if word == 1:
        return 0b10

    curr_lsb: int = 0
    prev_lsb: int = 0
    word_: int = word

    def bit_pos(word: int) -> int:
        return int(math.log2(word))

    while word_ != 0:
        curr_lsb = word_ & ~(word_ - 1)  # extract least significant bit
        if curr_lsb > prev_lsb << 1:
            # Lowest set bit with unset left neighbor is `prev_lsb`, so swap
            # set and unset bit to get smallest diff with same weight
            return int(
                swap_bits(word, i=bit_pos(prev_lsb), j=bit_pos(prev_lsb) + 1)
            )
            # break

        prev_lsb = curr_lsb
        word_ = word_ & (word_ - 1)  # clear least significant bit

    return int(
                swap_bits(word, i=bit_pos(prev_lsb), j=bit_pos(prev_lsb) + 1)
            )
