# get all subsets of nums/chars in an array
# e.g [1,2,3] -> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

# O(n.2^n)
def subsets(nums: list[int]):
    result = []

    subset = []
    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        # call dfs INCLUDING nums[i]
        subset.append(nums[i])
        dfs(i+1)

        # cal dfs WITHOUT nums[i]
        subset.pop()
        dfs(i+1)

    dfs(0)
    return result

