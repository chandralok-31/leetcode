class Solution:
    def pivotInteger(self, n: int) -> int:
        arr=[i for i in range(1,n+1)]

        for i in range(len(arr)):
            if sum(arr[:i+1])==sum(arr[i:]):
                return i+1
        return -1

        