def min_rotated(nums: list[int]):
    l, r = 0, len(nums) - 1
    result = nums[0]

    while l <= r:
        if nums[l] < nums[r]: # meaning array is sorted
            result = min(result, nums[l])
            break
        else:
            middle = (l + r)//2
            result = nums[middle]
            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1
    return result


arr = [5, 6, 7, 8, 1, 2, 3, 4]
print(min_rotated(arr))