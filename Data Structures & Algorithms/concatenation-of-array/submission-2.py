# O(n) time, O(1) space
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         ans = nums
#         for i in range(len(nums)):
#             ans.append(nums[i])
#         return ans

# O(n) time, O(n) space, creates new list but does not mutate the original nums with the common pointer, like the last solution, so this is a safer solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2