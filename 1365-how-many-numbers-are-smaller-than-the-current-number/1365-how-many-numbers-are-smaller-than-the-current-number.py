class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # arr=[]
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #         if nums[j]<nums[i]:
        #             count+=1
        #     arr.append(count)
        # return arr
                
        dic1 = {}
        nums1 = sorted(nums, reverse=True)
        print(nums)
        print(nums1)
        for index in range(0, len(nums1) - 1):
            if nums1[index] == nums1[index + 1]:
                continue
            dic1[nums1[index]] = len(nums1) - index -1    
        dic1[nums1[-1]] = 0
        return([dic1[x] for x in nums])      