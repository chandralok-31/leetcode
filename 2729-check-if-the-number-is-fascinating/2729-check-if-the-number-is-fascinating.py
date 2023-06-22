class Solution:
    def isFascinating(self, n: int) -> bool:
        str1=str(n)+str(2*n)+str(3*n)
        if len(str1)!=9:
            return False
        arr=[1,2,3,4,5,6,7,8,9]
        for i in range(len(str1)):
            if int(str1[i]) in arr:
                arr.remove(int(str1[i]))
        return len(arr)==0
        