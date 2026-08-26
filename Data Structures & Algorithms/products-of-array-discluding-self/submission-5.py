# O(n^2) time comlexity, wrong solution for this question, cause it explicitely asked for O(n) time complexity
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         product = []
#         for i in range(len(nums)):
#             prefix_product = 1
#             postfix_product = 1
#             for j in range(0, i):
#                 prefix_product *= nums[j]
#             for k in range(i+1, len(nums)):
#                 postfix_product *= nums[k]
#             single_product = prefix_product * postfix_product
#             product.append(single_product)
#         return product


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output