class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digit(n):
            arr=[int(i) for i in str(n)]
            return sum(arr)
        d={}
        for i in range(1,n+1):
            x=sum_digit(i)
            if x in d:
                d[x].append(i)
            else:
                d[x]=[i]
        d1={}
        for i in d.values():
            if len(i) in d1:
                d1[len(i)]+=1
            else:
                d1[len(i)]=1

        mx=0
        for i in d1.keys():
            mx=max(mx,i)
        return d1[mx]
            
            
        