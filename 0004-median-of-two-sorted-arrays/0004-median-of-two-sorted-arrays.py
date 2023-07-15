class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=[]
        x=0
        y=0
        num=sorted(nums1+nums2)
        n=len(num)
        if n%2 !=0:
            x=n//2
            return num[x]
        else:
            x=(n//2-1)
            y=(n//2)
            return (num[x]+num[y])/2
        