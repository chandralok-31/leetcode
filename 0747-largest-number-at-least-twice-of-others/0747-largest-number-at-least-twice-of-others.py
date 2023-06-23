class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        x=nums.index(max(nums))
        print(x)
        nums.sort()
        
        if nums[-1]>=nums[-2]*2:
            return x
        else:
            return -1
        