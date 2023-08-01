class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        i=1
        count=0
        while(n>=5):
            
            n=n//5
            count+=n
            
        return count
        