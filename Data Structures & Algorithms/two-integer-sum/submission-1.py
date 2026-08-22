class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if (diff := target - n) in seen:
                return [seen[diff], i]
            seen[n] = i