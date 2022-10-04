def missing_number(nums:list, n):
    # using XOR
    # XOR ing same numbers gives 0
    sum = 0
    for i in range(n):
        sum += i
    for num in nums:
        sum -= num
    return sum

arr= [1,0,3]
n=4

print(missing_number(arr, n))
#space = O(1), time: O(n)

