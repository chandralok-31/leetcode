class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        res=list(set(nums))
        res.sort()
        print(res)
        if len(res)<3:
            return res[-1]
        return res[-3]
       
            

        