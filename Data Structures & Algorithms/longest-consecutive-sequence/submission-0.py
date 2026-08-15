class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        longest = 0
        streak_map = {}  # Stores length of consecutive sequence containing n

        for n in nums:
            if n in streak_map:
                continue

            # Get lengths of left and right neighboring sequences (if they exist)
            left = streak_map.get(n - 1, 0)
            right = streak_map.get(n + 1, 0)

            # Total length of the new merged sequence
            current_streak = left + right + 1
            longest = max(longest, current_streak)

            # Update the boundaries of the sequence
            streak_map[n] = current_streak
            streak_map[n - left] = current_streak
            streak_map[n + right] = current_streak

        return longest