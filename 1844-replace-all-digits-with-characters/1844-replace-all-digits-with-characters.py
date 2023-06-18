class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(s1,s2):
            x=ord(s1)+s2
            return chr(x)
        s=list(s)
        for i in range(1,len(s),2):
            s[i]=shift(s[i-1],int(s[i]))
        return "".join(s)
            
            
        