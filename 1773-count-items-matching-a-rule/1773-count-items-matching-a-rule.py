class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        d = {'type': 0, 'color': 1, 'name': 2}
      
        for i in range(len(items)):
            if items[i][d[ruleKey]]==ruleValue:
                count+=1
        return count
        
        