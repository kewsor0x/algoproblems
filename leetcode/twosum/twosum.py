from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, val in enumerate(nums):
            seen = target - val
            if seen in hashmap:
                return [idx, hashmap[seen]]
            hashmap[val] = idx


nums = [2, 7, 11, 15]
target = 9
result = Solution()
print(result.twoSum(nums, target))
