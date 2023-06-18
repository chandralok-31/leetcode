class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n=len(s)
        
        c1,c2=0,0
        for i in range(n):
            if i<(n//2):
                if s[i] in x:
                    c1+=1
            else:
                if s[i] in x:
                    c2+=1
        return c1==c2
        