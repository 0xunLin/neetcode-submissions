import heapq

# O(n.logn) time, O(1) space
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heapq.heapify(nums)
#         for i in range(len(nums)-k):
#             heapq.heappop(nums)
#         return heapq.heappop(nums)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]