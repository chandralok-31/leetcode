class Solution:
    def tribonacci(self, n: int) -> int:
       
        m={0:0,1:1,2:1}
        for i in range(3,n+1):
            m[i]=m[i-1]+m[i-2]+m[i-3]
        return m[n]
        