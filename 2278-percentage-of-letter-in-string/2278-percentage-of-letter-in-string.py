class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n=len(s)
        x=s.count(letter)
        res=(x*100)//n
        return res
        