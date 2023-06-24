class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for num in nums: 
            res += [ i + [num] for i in res if i + [num] not in res]
        return res
            
                

