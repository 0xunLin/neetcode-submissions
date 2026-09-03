class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        left = 0
        max_len = 0
        max_freq = 0
        for right in range(len(s)):
            count_map[s[right]] = count_map.get(s[right], 0) + 1 # Update running state
            max_freq = max(max_freq, count_map[s[right]])
            while (right - left + 1) - max_freq > k: # Invalid state, so remove left element and increment left state
                count_map[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1) # Updating count
        return max_len