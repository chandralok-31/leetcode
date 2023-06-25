class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left=right=2
        # while right<len(nums):
        #     if nums[right]!=nums[left-2]: 
        #         nums[left]=nums[right]
        #         left+=1
        #     right+=1
        # return left
        l=2
        for r in range(2,len(nums)):
            if nums[r]!=nums[l-2]:
                nums[l]=nums[r]
                l+=1
        return l
            