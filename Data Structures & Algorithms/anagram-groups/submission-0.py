import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hashmap = collections.defaultdict(list)

        for string in strs:
            sorted_string_key = "".join(sorted(string))

            anagram_hashmap[sorted_string_key].append(string)

        return list(anagram_hashmap.values())