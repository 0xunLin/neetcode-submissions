# Horizontal scanning solution, shrinking prefix, O(n*m^2) time, O(m) space complexity
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         prefix = strs[0]
#         for word in strs[1:]:
#             while not word.startswith(prefix):
#                 prefix = prefix[:-1]
#         return prefix

# Vertical scanning solution, column checker, O(n*m) time, O(1) auxiliary space complexity
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
        return strs[0]
