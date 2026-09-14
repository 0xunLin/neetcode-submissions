import heapq

# O(n.logn) time, O(1) space
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heapq.heapify(nums)
#         for i in range(len(nums)-k):
#             heapq.heappop(nums)
#         return heapq.heappop(nums)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return heapq.nlargest(k, nums)[-1]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k] # Initialize a min-heap with the first k elements
        heapq.heapify(min_heap)
        for num in nums[k:]: # Iterate through the rest of the numbers
            if num > min_heap[0]: # If the current number is larger than the smallest in our heap
                heapq.heapreplace(min_heap, num) # Efficiently push the new number and pop the smallest out
        return min_heap[0] # The root of the heap is now the kth largest element