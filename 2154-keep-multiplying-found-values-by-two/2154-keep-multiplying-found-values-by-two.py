class Solution:
    def findFinalValue(self, nums: List[int], o: int) -> int:
        if o not in nums:
            return o
        else:
            return self.findFinalValue(nums,o*2)
        