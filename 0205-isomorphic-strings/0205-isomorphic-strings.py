class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in range(len(s)):
            if t[i] not in d:
                if s[i] in d.values():
                    return False
                d[t[i]]=s[i]
            else:
                if d[t[i]]!=s[i]:
                    return False
        return True
        