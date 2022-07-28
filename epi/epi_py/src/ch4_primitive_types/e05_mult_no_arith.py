# ### 4.5 Compute x * y without arithmetical operators ###

# """
# Sometimes the processors used in ultra low-power devices such as hearing aids do not have
# dedicated hardware for performing multiplication. A program that needs to perform multiplication
# must do so explicitly using lower-level primitives.

# Write a program that multiplies two nonnegative integers. The only operators you are allowed to
# use are
# • assignment,
# • the bitwise operators >>, <<, | &, ~ and
# • equality checks and Boolean combinations thereof.

# You may use loops and functions that you write yourself. These constraints imply, for example,
# that you cannot use increment or decrement, or test if x < y.

# Hint: Add using bitwise operations; multiply using shift-and-add.
# """

# from utils import Infix

# @Infix
# def multBy(x: int, y: int) -> int:
#     """
#     @x@: Non-negative integer
#     @y@: Non-negative integer
#     """
#     return x * y

# def add(x: int, y: int) -> int:
#     """
#     @x@: Non-negative integer
#     @y@: Non-negative integer
#     """
#     match x, y:
#         case _, 0: return x
#         case 0, _: return y
#         case n, 1:
#             lsb = n & ~(n - 1)
#             if lsb != 0b1:  # ex. 0b0 -> 0b1, 0b11000 -> 0b11001
#                 return n | 0b1
#             else:  # ex. 0b1011 -> 0b11011
#                 return n | lsb >> 1 ^ 0  ## FIXME more like bin((0b1011 | 2 ** msb(0b1011) >> 1) ^ 1)
#         case n, m:


#         #         # If n is even, add 1
#         #         case 0: return n | 0b1
#         #         # If n is odd, 
#         #         case _: return 2
#         # case _: return add(x, y - 1)

#     #         if  != 0b1:
#     #             return p | 0b1
#     #         else:
#     #             return p
#     #     case 1, n: return add(x, 1)

#     # return x * y