class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        def sum1(a):
            sm=0
            for i in a:
                sm+=i
            return sm
        mx=0
        for i in accounts:
            mx=max(sum1(i),mx)
        return mx
            
        