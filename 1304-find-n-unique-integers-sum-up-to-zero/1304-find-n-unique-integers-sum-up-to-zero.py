class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr=[]
        i=1
        j=-1
        
        if n%2!=0:
            arr.append(0)

            while n-1>0:
                arr.append(i)
                arr.append(j)
                i+=1
                j-=1
                n-=2
        else:
            while n>0:
                arr.append(i)
                arr.append(j)
                i+=1
                j-=1
                n-=2
        return arr
            
            
        