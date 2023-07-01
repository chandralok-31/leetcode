class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x=1
        for i in nums:
            x=x*i
        if x==0:
            return 0
        elif x>0:
            return 1
        else:
            return -1