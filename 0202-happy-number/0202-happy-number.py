class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        summ=0
        if n==1:
            return True
        if n==4:
            return False
        
        while n>0:
            summ+=(n%10)**2
            n=n//10
        
        n=summ
        return self.isHappy(n)
        
        
    
    
    

    
    
    
    
    
    
    
    
    
    
    
                    
            
            
        