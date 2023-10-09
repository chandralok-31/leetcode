class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a=0
        for i in range(len(spaces)):
            x=spaces[i]+a
            a=a+1
            s=s[:x]+" "+s[x:]
        return s

        
        
        