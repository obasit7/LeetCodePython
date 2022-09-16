arr = [-3, 3, 4, -3, 1, 2]

# Time: O(n^2) Space: O(1) or O(n)

def threeSum(nums):
    nums.sort()
    res = []

    for i, a in enumerate(nums):
        #skip if duplicate num
        if i>0 and a == nums[i-1]:
            continue
        l, r = i+1, len(nums) - 1
        while l < r:
            sum = a + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum <0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l<r:
                    l += 1

    return res


print(threeSum(arr))

