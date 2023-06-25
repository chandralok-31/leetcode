class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        a_start,a_end=event1[0],event1[1]
        b_start,b_end=event2[0],event2[1]
        return b_start<=a_start<=b_end or b_start<= a_end<=b_end or a_start<= b_start<=a_end or a_start<= b_end<=a_end
        