class Solution:
    def maxPower(self, s: str) -> int:
        local_max, global_max = 1, 1
        prev='#'
        for i in s:
            if i==prev:
                local_max+=1
                global_max = max( global_max, local_max )
            else:
                local_max=1
                prev=i

        
        
        return global_max