class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        n1=n//4
        for i in arr:
            if arr.count(i)>n1:
                return i
        
        