class Solution:
    def capitalizeTitle(self, title: str) -> str:
        x=title.split()
        print(x)
        for i in range(len(x)):
            if len(x[i])==1 or len(x[i])==2:
                x[i]=x[i].lower()
                
            else:
                x[i]=x[i].capitalize()

            
        return " ".join(x)
        
        