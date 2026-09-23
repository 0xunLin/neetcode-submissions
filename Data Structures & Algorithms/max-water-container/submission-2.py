class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_amount = 0
        while left < right:
            breadth = right-left
            tall = min(heights[left], heights[right])
            amount = breadth * tall
            max_amount = max(max_amount, amount)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_amount
