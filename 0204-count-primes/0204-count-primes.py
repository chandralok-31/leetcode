class Solution:
    def countPrimes(self, num: int) -> int:
        if num==0 or num==1 or num==2:
            return 0

    
        prime = [i for i in range(num)]
        prime[0]=0
        prime[1]=0

        p = 2
        while (p * p <= num):

            if (prime[p]!=0):

                # Updating all multiples of p
                for i in range(p * p, num, p):
                    prime[i] = 0
            p += 1
        count=0
        for p in range(2, num):
            if prime[p]:
                count+=1
        return count
                
        