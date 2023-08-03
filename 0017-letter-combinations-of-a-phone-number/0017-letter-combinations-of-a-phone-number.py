class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d={'2':['a','b','c'],
           '3':['d','e','f'],
           '4':['g','h','i'],
           '5':['j','k','l'],
           '6':['m','n','o'],
           '7':['p','q','r','s'],
           '8':['t','u','v'],
           '9':['w','x','y','z']}
        if len(digits)==0:
            return []
        if len(digits)==1:
            return d[digits[0]]
        
        arr=[]
        for i in d[digits[0]]:
            
            for j in self.letterCombinations(digits[1:]):
                str1=""
                str1+=i+j
                arr.append(str1)
        print(arr)
        return arr