#
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# from collection import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t): 
#             return False
#         count = [0] * 26
#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1
#         return all(x == 0 for x in count)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            seen[t[i]] = seen.get(t[i], 0) - 1
        return all(x == 0 for x in seen.values()) # .values() to iterate over the values not the keys