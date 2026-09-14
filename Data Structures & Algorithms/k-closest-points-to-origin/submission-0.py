import heapq

# O(n.logk) time, O(k) space
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         max_heap = [] 
#         for x, y in points:
#             distance = -(x**2 + y**2) ** 0.5
#             heapq.heappush(max_heap, (distance, [x, y]))

#             if len(max_heap) > k:
#                 heapq.heappop(max_heap)
#         return [point for distance, point in max_heap] # Once the loop finishes, the heap holds exactly the k closest points. This line uses a list comprehension to extract just the [x, y] coordinates from the tuples, discarding the distance values, and returns the final list.

# O(n.logn) time, O(n) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2) # key=lambda p: ... part tells Python exactly how to compare two points

        return points[:k]