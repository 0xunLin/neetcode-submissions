from collections import deque

# O(n * k) high time complexity, TLE
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         a = []
#         for i in range(0, len(nums)-k+1):
#             a.append(max(nums[i: i + k]))
#         return a

# O(n) time, O(k) space
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        index = deque()
        result_queue = []
        for i in range(len(nums)):
            if index and index[0] < i-k+1:
                index.popleft()
            while index and nums[index[-1]] < nums[i]:
                index.pop()
            index.append(i)
            if i >= k-1:
                result_queue.append(nums[index[0]])
        return result_queue

# There is a O(n) time, O(1) space solution using two [0] * len(nums) size lists 
