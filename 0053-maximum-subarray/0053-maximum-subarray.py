class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum=nums[0]
        cursum=0
        for i in range(len(nums)):
            cursum+=nums[i]
            if maxsum<cursum:
                maxsum=cursum
            if cursum<0:
                cursum=0
        return maxsum
            
                
            
        
        