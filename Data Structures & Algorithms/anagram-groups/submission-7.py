import collections

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_hashmap = collections.defaultdict(list)

#         for string in strs:
#             sorted_string_key = "".join(sorted(string))

#             anagram_hashmap[sorted_string_key].append(string)

#         return list(anagram_hashmap.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hashmap = collections.defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1
                
            anagram_hashmap[tuple(count)].append(string)

        return list(anagram_hashmap.values())


# Robust solution to include UPPERCASE letters and emojis
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_hashmap = collections.defaultdict(list)

#         for string in strs:
#             count_map = collections.Counter(string)

#             signature = tuple(sorted(count_map.items()))

#             anagram_hashmap[signature].append(string)

#         return list(anagram_hashmap.values())