from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in range(len(strs)):
            current = "".join(sorted(strs[i]))

            if current not in hashmap:
                hashmap[current] = [strs[i]]
            else:
                hashmap[current].append(strs[i])

        return list(hashmap.values())
