class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        numset = set(nums)
        for i in nums:

            if i-1 not in numset:
                length = 0

                while (i+length) in numset:
                    length += 1

                max_length = max(length, max_length)

        return max_length
