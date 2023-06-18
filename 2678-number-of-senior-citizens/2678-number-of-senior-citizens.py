class Solution:
    def countSeniors(self, d: List[str]) -> int:
        count=0
        for i in range(len(d)):
            if int(d[i][11:13])>60:
                count+=1
        return count
        