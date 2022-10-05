# given 32 bit number, reverse its bits

def reverse_bits(n: int):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        result = result | (bit << (31 - i))

    return result
#O(1) time and space
print(reverse_bits(10))