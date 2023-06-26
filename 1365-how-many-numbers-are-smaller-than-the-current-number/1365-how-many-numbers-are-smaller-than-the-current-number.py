class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            arr.append(count)
        return arr
                
#         arr={i:nums.index(i) for i in nums}
#         print(arr)
        
#         arr.sort()
#         res=[]
#         for  i in range(len(arr)):
#             x=arr.index(nums[i])
#             res.append(x)
        
#         return res       