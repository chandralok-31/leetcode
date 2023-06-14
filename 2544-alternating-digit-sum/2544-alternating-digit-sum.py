class Solution:
    def alternateDigitSum(self, n: int) -> int:
        summ=0
        arr=[int(x) for x in str(n)]
        n=len(arr)
        for i in range(n):
            if i%2==0:
                summ+=arr[i]
            else:
                summ=summ-arr[i]
        return summ
        