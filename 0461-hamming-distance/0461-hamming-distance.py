class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x='{0:032b}'.format(x)
        y='{0:032b}'.format(y)
        count=0
        for i in range(len(x)):
            if x[i]!=y[i]:
                count+=1
        return count
            
        