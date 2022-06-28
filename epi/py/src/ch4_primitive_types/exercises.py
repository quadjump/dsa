def count_bits(x: int) -> int:
    """
    @x@: Decimal number whose number of set bits in binary form we want
    :returns: Number of set bits in binary form of `x`
    """
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits