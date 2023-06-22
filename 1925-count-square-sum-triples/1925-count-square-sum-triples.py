class Solution:
    def countTriples(self, n: int) -> int:
        cnt=0
        for i in range(1,n):
            for j in range(1+i,n):
                x=i*i+j*j
                s= math.sqrt(x)
                if int(s)==s and s<=n:
                    cnt+=2
        return cnt
    
    
