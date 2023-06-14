class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            str1=""
            while nums[i]>0:
                str1+=str(nums[i]%10)
                nums[i]=nums[i]//10
            
            for j in range(len(str1)-1,-1,-1):
                res.append(int(str1[j]))

        return res