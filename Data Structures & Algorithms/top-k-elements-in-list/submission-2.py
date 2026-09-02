class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = [(freq, num) for num, freq in count.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)

        return [v for k, v in heap]
        