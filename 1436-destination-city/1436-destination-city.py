class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        source=p[0][0]
        d={source:destination for source,destination in p}
        
        current=source
        while current in d:
            current=d[current]
        return current
            

                
            
            
        