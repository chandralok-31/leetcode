class Solution:
    def countEven(self, num: int) -> int:
        
        def digitsum(n):
            summ=0
            while n>0:
                summ+=n%10
                n=n//10
            if summ%2==0:
                return True
            else:
                return False
            
        count=0
        for i in range(1,num+1):
            if digitsum(i):
                count+=1
        return count
        