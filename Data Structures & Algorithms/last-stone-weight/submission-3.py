import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = [-stone for stone in stones]
        heapq.heapify(a)
        while len(a) > 1:
            s1 = heapq.heappop(a)
            s2 = heapq.heappop(a)
            if s1 != s2:
                heapq.heappush(a, s1-s2)
        return -a[0] if a else 0