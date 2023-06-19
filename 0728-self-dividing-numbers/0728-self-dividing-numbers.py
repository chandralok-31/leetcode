class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def divide(n):
            x=[]
            for i in str(n):
                if int(i)==0:
                    return False
                else:
                    x.append(int(i))

            count=0
            for i in x:
                if n%i!=0:
                    return False
            return True
        arr=[]
        for i in range(left,right+1):
            if divide(i):
                arr.append(i)
        return arr
        