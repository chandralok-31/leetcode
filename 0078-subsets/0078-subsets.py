class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets
                
        