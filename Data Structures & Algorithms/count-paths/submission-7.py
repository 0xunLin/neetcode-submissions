# O(m * n) time, O(m * n) space
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def memoization(r: int, c: int, m: int, n: int, cache):
#             if r == m or c == n:
#                 return 0
#             if cache[r][c] > 0:
#                 return cache[r][c]
#             if r == m - 1 and c == n - 1:
#                 return 1
#             cache[r][c] = memoization(r + 1, c, m, n, cache) + memoization(r, c + 1, m, n, cache)
#             return cache[r][c]
#         return memoization(0, 0, m, n, [[0] * n for i in range(m)])

# O(m * n) time, O(min(m, n)) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i, j = 0, 0
        if m <= n:
            i = m
            j = n
        else:
            i = n
            j = m
        prevRow = [0] * j
        for r in range(i-1, -1, -1):
            currRow = [0] * j
            currRow[j - 1] = 1
            for c in range(j-2, -1, -1):
                currRow[c] = currRow[c + 1] + prevRow[c]
            prevRow = currRow
        return prevRow[0]