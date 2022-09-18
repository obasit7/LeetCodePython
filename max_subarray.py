arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_sum_subarray(arr):
    max_sum = arr[0]
    curr_sum = 0

    for n in arr:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sum = max(max_sum, curr_sum)

    return max_sum
