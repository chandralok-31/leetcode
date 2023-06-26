class Solution:
    import math
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def primeFactors(n):
            factor=set()
            d=2
            while d*d<=n:
                while n%d==0:
                    factor.add(d)
                    n=n/d
                d+=1
            if n>1:
                factor.add(n)
            return factor
        ans=set()
        for i in range(len(nums)):
            ans|=primeFactors(nums[i])
            
        return len(ans)



        