import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        h.heapify_max(heap)
        while len(stones)>1:
            s1 = h.heappop_max(heap)
            s2 = h.heappop_max(heap)
            if(s1 > s2):
                h.heappush_max(heap, s1 - s2)
        return heap[0] if heap else 0