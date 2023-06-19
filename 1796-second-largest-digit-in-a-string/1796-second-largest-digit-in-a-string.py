class Solution:
    def secondHighest(self, s: str) -> int:
        res=[]
        for i in range(len(s)):
            if s[i].isnumeric():
                if int(s[i]) not in res:
                    res.append(int(s[i]))
        res.sort()
        if len(res)==0 or len(res)==1:
            return -1
        else:
            return res[-2]
            
        