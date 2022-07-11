import bitstring as bs
from bitstring import BitArray, BitStream

def get_bit(ba: BitArray, n: int) -> bool:
    """
    Returns true if bit is set
    """
    return bool(ba[n])

def set_bit(ba: BitArray, n: int) -> BitArray:
    """
    Returns bit string with nth bit set to 1
    """
    bs.overwrite(1, n)
    return ba

def clear_bit(ba: BitArray, n: int) -> BitArray:
    ba.overwrite(0, n)
    return ba

def clear_least_bit(ba: BitArray) -> BitArray:
    ba & (ba - 1)
