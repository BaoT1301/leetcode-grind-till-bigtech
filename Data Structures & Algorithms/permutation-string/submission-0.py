class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        for s in s1:
            if s in count1:
                count1[s] += 1
            else:
                count1[s] = 1

        l = 0
        for r in range(len(s2)):
            if s2[r] in count2:
                count2[s2[r]] += 1
            else:
                count2[s2[r]] = 1
            
            if r - l + 1 > len(s1):
                count2[s2[l]] -= 1

                if count2[s2[l]] == 0:
                    del count2[s2[l]]

                l += 1

            if count1 == count2:
                return True
            
        return False
