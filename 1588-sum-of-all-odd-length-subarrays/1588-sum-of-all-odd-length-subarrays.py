class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarrays = []
        n = len(arr)
        sm=0
        for i in range(n):
            for j in range(i+1, n+1):
                if len(arr[i:j])%2!=0:
                    sm+=sum(arr[i:j])
        return sm
                

        