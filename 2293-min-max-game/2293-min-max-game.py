class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        else:
            newNums=[0]*(n//2)
        for i in range(0,n//2,2):
            newNums[i]=min(nums[2*i],nums[2*i+1])
        for i in range(1,n//2,2):
            newNums[i]=max(nums[2*i],nums[2*i+1])
        nums=newNums
        return self.minMaxGame(nums)

        