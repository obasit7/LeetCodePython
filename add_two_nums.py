# adding 2 nums without using + or -

def add(n1, n2):
    while n2 != 0:
        carry = (n1 & n2) << 1
        n1 = n1 ^ n2
        n2 = carry
    return n1

print(add(4,6))
