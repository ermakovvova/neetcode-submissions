class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_idxs = set()
        for i, num in enumerate(nums):
            if num != 0:
                prod *= num
            else:
                zero_idxs.add(i)

        res = []
        if len(zero_idxs) > 1:
            return [0] * len(nums)
        elif len(zero_idxs) == 1:
            res = [0] * len(nums)
            res[zero_idxs.pop()] = prod
        else:
            for num in nums:
                res.append(int(prod / num))

            
        return res        