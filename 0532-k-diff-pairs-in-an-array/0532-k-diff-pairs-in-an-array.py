class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # return the number of unique pairs
        answ=0
        # create a dictionary: d[x]==nums.count(x)
        d={}
        for x in nums:
            if x in d: d[x]+=1
            else:      d[x]=1
        
        if k>0: # k>0
            answ=sum(x+k in d for x in d.keys())
        else: # k==0
            answ=sum(k>1 for k in d.values())
                
        return answ
    
        # count=0
        # d={}
        # for i in nums:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # if k>0:
        #     count=sum([i+k in d for i in d.keys()])
        # else:
        #     count=sum([k>1 for i in d.values()])
        # return count
            
