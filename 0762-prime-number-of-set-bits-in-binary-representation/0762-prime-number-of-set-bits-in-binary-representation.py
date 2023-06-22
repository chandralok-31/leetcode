class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime(n):
            if n<=1:
                return 0
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return 0
            return 1
        arr=[]
        for i in range(left,right+1):
            x=bin(i)
            arr.append(x[2:].count('1'))
        cnt=[prime(i) for i in arr]
        return sum(cnt)
        
        
        