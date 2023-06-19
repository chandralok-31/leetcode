class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mm=min(nums)
        mx=max(nums)
        for i in range(mm,0,-1):
            if mm%i==0 and mx%i==0:
                return i
        return 1
        

        