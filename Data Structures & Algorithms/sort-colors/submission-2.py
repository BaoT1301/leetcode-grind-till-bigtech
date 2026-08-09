class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1 = 0
        count2 = 0
        count0 = 0
        
        for num in nums:
            if num == 1:
                count1 += 1
            elif num == 2:
                count2 += 1
            elif num == 0:
                count0 += 1
        i = 0
        for k in range(count0):
            nums[i] = 0
            i += 1

        for k in range(count1):
            nums[i] = 1               
            i += 1

        for k in range(count2):
            nums[i] = 2
            i += 1

        return nums
            
