class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# 3 4 5 6
# 3 -> 7 - 3 = 4
# map[3] = 0
# target - nums[1] in map[3] -> return i, j
        el2pos = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in el2pos:
                return [el2pos[compl], i]
            if nums[i] not in el2pos:
                 el2pos[nums[i]] = i




        