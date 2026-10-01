# O(n) time, O(1) space
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         ans = nums
#         for i in range(len(nums)):
#             ans.append(nums[i])
#         return ans

# O(1) time, O(1) space
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2