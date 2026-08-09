class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for str in strs:
            sorted_str = "".join(sorted(str))

            if sorted_str in hash:
                hash[sorted_str].append(str)
            else:
                hash[sorted_str] = []
                hash[sorted_str].append(str)


        return list(hash.values())