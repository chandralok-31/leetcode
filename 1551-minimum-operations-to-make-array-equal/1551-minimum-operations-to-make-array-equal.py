class Solution:
    def minOperations(self, n: int) -> int:
        arr=[(2*i+1) for i in range(n)]
        target=sum(arr)//n
        cnt=0
        for i in range(n//2):
            cnt+=target-arr[i]
        return cnt
                    
#         arr=[(2*i+1) for i in range(n)]
#         target=sum(arr)//n
#         i=0
#         j=n-1
#         count=0
#         while i<j:
#             if arr[i]!=target and arr[j]!=target:

#                 arr[i]+=1
#                 arr[j]-=1
#                 count+=1
#             else:
#                 i+=1
#                 j-=1
#         return count
            
        