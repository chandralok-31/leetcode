class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        mx=max(candies)
        for i in range(len(candies)):
            x= candies[i]+extraCandies
            if x>=mx:
                res.append(True)
                
            else:
                res.append(False)
        return res
        