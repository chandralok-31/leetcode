class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digit=[]
        while n:
            n,rem=divmod(n,k)
            digit.append(str(rem))
        num=[int(i) for i in digit]
        return sum(num)
        
        
        