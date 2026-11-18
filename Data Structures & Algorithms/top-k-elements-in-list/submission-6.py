class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, c in count.items():
            heapq.heappush(heap, (c, num))

        while len(heap) > k:
            heapq.heappop(heap)

        return [num for c, num in heap]

        