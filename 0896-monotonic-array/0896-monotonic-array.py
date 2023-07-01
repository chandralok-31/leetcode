class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if (nums[-1]-nums[0])>=0:
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1]<0:
                    return False
            return True
        else:
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1]>0:
                    return False
            return True                   
        