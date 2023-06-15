class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        arr1=[]
        for i in range(1,a+1):
            if a%i==0:
                arr1.append(i)
        arr2=[]
        for i in range(1,b+1):
            if b%i==0:
                arr2.append(i)
        return len([value for value in arr1 if value in arr2])
 
