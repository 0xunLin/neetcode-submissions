# O(nlogn) time, O(n) space, due to timsort's linear space
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# O(n) time, O(n) space
# from collection import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

# O(n) time, O(1) space for only lowercase strings(in this case), O(n) space if arbitrary unicode
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t): 
#             return False
#         seen = {}
#         for i in range(len(s)):
#             seen[s[i]] = seen.get(s[i], 0) + 1
#             seen[t[i]] = seen.get(t[i], 0) - 1
#         return all(x == 0 for x in seen.values()) # .values() to iterate over the values not the keys

# O(n) time, O(1) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        return all(x == 0 for x in count)