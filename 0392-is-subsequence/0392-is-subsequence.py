class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr=""
        j=0
        for i in range(len(t)):
            if t[i] in s and t[i]==s[j]:
                arr+=t[i]
                j+=1
        return s==arr
        