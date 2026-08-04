class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, e in enumerate(nums):
            if (difference := target - e) in seen:
                return [seen[difference], i]
            seen[e] = i