class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        x=[ i for i in nums1 if i in nums2 ]
        if len(x)!=0:
            return x[0]

        else:
            if nums1[0]<nums2[0]:
                return int(str(nums1[0])+str(nums2[0]))
            else:
                return int(str(nums2[0])+str(nums1[0]))
                