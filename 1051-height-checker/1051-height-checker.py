class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        d={}
        for i,n in enumerate(heights):
            d[i]=n
        count=0
        heights.sort()
        for i in range(len(heights)):
            if heights[i]!=d[i]:
                count+=1
        return count
        