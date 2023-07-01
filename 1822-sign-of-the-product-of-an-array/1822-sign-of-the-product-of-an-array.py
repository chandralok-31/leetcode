class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x=1
        for i in nums:
            if i==0:
                return 0
            if i>0:
                x=x*1
            else:
                x=x*(-1)
        return x
