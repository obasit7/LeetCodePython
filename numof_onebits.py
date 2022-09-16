n = 100011

res = 0

while n:
    n &= (n-1)
    res += 1

print(res)