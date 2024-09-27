class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for i in nums:
            d[i] +=1

        heap = []
        
        for key, value in d.items():
            heapq.heappush(heap, (-value, key))

        while k > 0:
             res.append(heapq.heappop(heap)[1])
             k -= 1
        
        return res 