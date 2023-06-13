class Solution:
    def reverseWords(self, s: str) -> str:

        x=s.split()
        x=x[::-1]
        
        str1=""
        for i in range(len(x)):
            str1+=x[i]
            if i<len(x)-1:
                str1+=" "

        return str1
        