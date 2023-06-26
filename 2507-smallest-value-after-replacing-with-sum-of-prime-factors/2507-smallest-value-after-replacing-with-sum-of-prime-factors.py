class Solution:
    def smallestValue(self, n: int) -> int:


        prev, ans = n, 0

        while not n%2:                 
                ans += 2
                n//= 2

        for i in range(3,n+1,2):       
                while not n%i:
                    ans += i
                    n//= i

        return self.smallestValue(ans) if ans != prev else ans

            

                
                    
        