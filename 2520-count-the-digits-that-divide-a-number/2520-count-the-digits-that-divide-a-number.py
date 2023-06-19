class Solution:
    def countDigits(self, num: int) -> int:
        str1=[int(i) for i in str(num)]
        count=0
        for i in str1:
            if num%i==0:
                count+=1
        return count
        