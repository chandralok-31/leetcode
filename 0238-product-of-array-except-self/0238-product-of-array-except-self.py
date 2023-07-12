class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        for i in range(len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
        if nums.count(0)>1:
            for i in range(len(nums)):
                nums[i]=0
            return nums
        if nums.count(0)==1:
            idx=nums.index(0)
            for i in range(len(nums)):
                if i==idx:
                    nums[idx]=prod
                else:
                    nums[i]=0
            return nums
        for i in range(len(nums)):
            nums[i]=prod//nums[i]
        return nums
            
            
        