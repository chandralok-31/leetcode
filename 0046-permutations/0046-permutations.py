class Solution:
    from itertools import permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if len(nums)==0:
        #     return []
        # if len(nums)==1:
        #     return [nums]
        # l=[]
        # for i in range(len(nums)):
        #     m=nums[i]
        #     remList=nums[:i]+nums[i+1:]
        #     for p in self.permute(remList):
        #         l.append([m]+p)
        # return l
        p = list(permutations(nums))
        return p
        




