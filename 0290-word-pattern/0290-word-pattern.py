class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s1=list(pattern)
        s2=s.split()
        d={}
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if s2[i] not in d:
                if s1[i] in d.values():
                    return False
                d[s2[i]]=s1[i]
            else:
                
                if d[s2[i]]!=s1[i]:
                    return False
        return True
                
            
        