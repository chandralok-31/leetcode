class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        count=0
        for j in t:
            if (j in d) and d[j]>0:
               
                d[j]-=1
         
            else:
                count+=1
       
        return sum(d.values())

    

