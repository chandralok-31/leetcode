class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]+nums[:-1]
        rightsum=nums[1:]+[0]
        print(leftsum)
        print(rightsum)
        summ=[]
        l=[]
        
        for i in range(len(nums)):
            l.append(sum(leftsum[:i+1]))
        r=[]
        rightsum.reverse()
        for i in range(len(nums)):
            r.append(sum(rightsum[:i+1]))
        r.reverse()
        for i in range(len(nums)):
            summ.append(abs(r[i]-l[i]))
        return summ
        
        
        
        