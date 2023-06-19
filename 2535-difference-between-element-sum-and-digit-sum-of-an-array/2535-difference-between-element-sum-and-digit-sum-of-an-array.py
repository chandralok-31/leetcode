class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            x=[int(i) for i in str(n)]
            return sum(x)
        ele_sm=0
        d_sm=0
        for i in range(len(nums)):
            ele_sm+=nums[i]
            d_sm+=digit_sum(nums[i])
        return abs(ele_sm-d_sm)
            
        