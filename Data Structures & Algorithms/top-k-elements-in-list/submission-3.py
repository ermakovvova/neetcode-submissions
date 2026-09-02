class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        cnt = 0
        i = len(freq) - 1
        while i > 0 and cnt < k:
            if len(freq[i]) > 0:
                j = 0
                while j < len(freq[i]) and cnt < k:
                    res.append(freq[i][j])
                    cnt += 1
                    j += 1
            i -= 1

        return res


        