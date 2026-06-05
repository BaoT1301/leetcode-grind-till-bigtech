class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for str1 in strs:
            sorted_s = ''.join(sorted(str1))

            if sorted_s not in group:
                group[sorted_s] = []
            group[sorted_s].append(str1)

        return list(group.values())
            

