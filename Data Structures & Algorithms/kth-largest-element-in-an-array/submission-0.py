import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                h.heappush(heap, num)
            elif num > heap[0]:
                h.heapreplace(heap, num)
        return heap[0]
