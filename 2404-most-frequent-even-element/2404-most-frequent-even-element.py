class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                res.append(nums[i])
        x=sorted(sorted(res),reverse=1,key=res.count)
        print(x)
        if len(x)>0:
            return x[0]
        else:
            return -1