class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=bin(n)
        y=x[2:]
        for i in range(1,len(y)):
            if y[i-1]==y[i]:
                return False
        return True
        