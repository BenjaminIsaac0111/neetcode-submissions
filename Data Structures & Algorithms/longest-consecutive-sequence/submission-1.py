class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        
        for n in nums:
            if (n - 1) not in hash_set:
                lenght = 0
                while (n + lenght) in hash_set:
                    lenght += 1
                longest = max(longest, lenght)
        return longest