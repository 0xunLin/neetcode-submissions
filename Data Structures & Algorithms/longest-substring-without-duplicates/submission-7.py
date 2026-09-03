class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        length = 0
        for right in range(len(s)):
            while s[right] in seen: # Invalid state so, remove left element and increment left
                seen.remove(s[left])
                left += 1
            seen.add(s[right]) # Updating the running state
            length = max(length, right-left+1) # maximum window size between length and the possible new window
        return length