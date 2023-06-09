class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=s.split()
        if len(arr[-1])==0:
            arr.remove(arr[-1])
        return len(arr[-1])
        