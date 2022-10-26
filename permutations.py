# uses backtracking e.g [ 1, 2, 3 ]
#               ->  1      2       3
#                [2 3]   [1 3]   [1 2]
#              [3] [2]  [3] [1]  [2] [1]
#
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums.copy()]

        result = []

        for i in range(len(nums)):
            n = nums.pop(0) # remove one from sublist
            perms = self.permute(nums) # take perms of modified array
            for perm in perms:
                perm.append(n) # add removed numebr back
            result.extend(perms)
            nums.append(n)

        return result
