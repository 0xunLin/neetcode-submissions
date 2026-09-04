# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         ws = len(s1)
#         if ws > len(s2):
#             return False
#         left = 0
#         s1_count = [0] * 26
#         s2_count = [0] * 26
#         for i in range(ws):
#             s1_count[ord(s1[i]) - ord('a')] += 1
#             s2_count[ord(s2[i]) - ord('a')] += 1
#         if s1_count == s2_count:
#             return True
#         for right in range(ws, len(s2)):
#             s2_count[ord(s2[right]) - ord('a')] += 1
#             s2_count[ord(s2[left]) - ord('a')] -= 1
#             left += 1
#             if s1_count == s2_count:
#                 return True
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ws = len(s1)
        if ws > len(s2):
            return False
        left = 0
        s1_count = {}
        s2_count = {}
        for i in range(ws):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        if s1_count == s2_count:
            return True
        for right in range(ws, len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]
            left += 1
            if s1_count == s2_count:
                return True
        return False