class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums=str(num)
        arr=[]
        for i in range(len(nums)):
            if len(nums[i:i+k])==k:
                arr.append(nums[i:i+k])
        print(arr)

        count=0
        for i in range(len(arr)):
            if int(arr[i])!=0:
                if num%int(arr[i])==0 :
                    count+=1
        return count
            
        