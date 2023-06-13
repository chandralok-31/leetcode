class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mydict={}
        res=set()
        for i in nums:
            mydict[i]=mydict.get(i,0)+1
            if mydict[i]>len(nums)//3:
                res.add(i)
        return list(res)


        