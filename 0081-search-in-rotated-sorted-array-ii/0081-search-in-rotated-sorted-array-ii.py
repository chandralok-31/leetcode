class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l=0
        h=len(nums)-1
        while h>=l:
            if(nums[l]==target or nums[h]==target):
                return True
            elif(target>nums[l]):
                while(l<h and nums[l+1]==nums[l]):
                    l+=1
                l+=1
            elif(target<nums[h]):
                while(l<h and nums[h-1]==nums[h]):
                    h-=1
                h-=1
            else:
                break
                    
        
        return False
        