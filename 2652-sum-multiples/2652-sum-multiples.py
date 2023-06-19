class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sm=0
        num=[i for i in range(1,n+1)]
 
        for i in (num):
            if i%3==0 or i%5==0 or i%7==0:
                sm+=i
        return sm
        