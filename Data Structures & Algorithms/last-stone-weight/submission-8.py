import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones] # heaps in python are naturally min-heap, so (-), to turn it into a max-heap
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)
        return -max_heap[0] if max_heap else 0

        