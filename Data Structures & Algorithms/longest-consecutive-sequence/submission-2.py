from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in nums:
                curr_len = 1
                curr = num
                while curr + 1 in nums:
                    curr_len += 1
                    curr += 1

                max_len = max(curr_len, max_len)

        return max_len

                


            



        