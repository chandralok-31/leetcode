class Solution:
    def addDigits(self, num: int) -> int:
        if num%10==num:
            return num
        res=0
        while num>0:
            res+=num%10
            num=num//10
        num=res
        return self.addDigits(num)
        