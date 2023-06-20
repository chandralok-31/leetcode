class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            x=bin(i)
            count=x.count('1')
            ans.append(count)
        return ans
        