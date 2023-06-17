class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count=0
        for i,w1 in enumerate(words):
            for w2 in words[i+1:]:
                count+=set(w1)==set(w2)
        return count 

        
                
            
        