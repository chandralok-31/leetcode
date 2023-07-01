class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        mx=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                mx=max(mx,count)
                count=0
        return max(mx,count)
                        
            