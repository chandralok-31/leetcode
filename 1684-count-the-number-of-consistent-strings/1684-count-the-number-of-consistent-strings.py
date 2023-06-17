class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        allowed=set(allowed)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    count+=1
                    break
            
        return len(words)-count
            
        