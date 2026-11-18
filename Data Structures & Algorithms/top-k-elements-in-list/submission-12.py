class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        n = max(count.values()) + 1
        # buckets = [[]] * n
        buckets = [[] for _ in range(n)]
        for num, c in count.items():
            buckets[c].append(num)

        res = []
        for bucket in buckets[n-1:0:-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        return res
                    
# 2: 4
# 1: 1
# 3: 5

        

        