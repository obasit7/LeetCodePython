arr = [-1, 2, -3, 0, 1, 5]
res = max(arr)
currMin, currMax = 1, 1

for n in arr:
    tmp = currMax*n # important
    currMax = max(n, currMin*n, currMax*n)
    currMin = min(n, currMin*n, tmp)
    # print(f"n: {n}, currMin: {currMin}, currMax: {currMax}")
    res = max(res, currMax)

print(res)
