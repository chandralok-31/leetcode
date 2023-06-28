class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d={}
        count=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for num in nums:
            if num+k in d:
                count+=d[num+k]
        return count
                
        