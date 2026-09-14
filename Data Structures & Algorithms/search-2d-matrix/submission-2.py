# O(n*m) time, O(n*m) space
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         li = []
#         for i in range(len(matrix)):
#             li += matrix[i]
#         l = 0
#         r = len(li) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if target < li[mid]:
#                 r = mid - 1
#             elif target > li[mid]:
#                 l = mid + 1
#             else:
#                 return True
#         return False

# O(log(n*m)) time, O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols) - 1
        while l <= r:
            mid = (l + r) // 2
            # Virtual indexing: map 1D index back to 2D coordinates
            row = mid // cols
            col = mid % cols
            if target < matrix[row][col]:
                r = mid - 1
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                return True
        return False