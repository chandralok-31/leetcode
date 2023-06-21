class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sm=0
        count=0
        for i in range(len(nums)):
            if nums[i]%6==0:

                sm+=nums[i]
                count+=1
        if count==0:
            return 0
        else:
            return sm//count
        