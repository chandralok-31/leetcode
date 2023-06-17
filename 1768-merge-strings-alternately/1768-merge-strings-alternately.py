class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1=""
        n1=len(word1)
        n2=len(word2)
        i=0
        j=0
        while n1>0 and n2>0:
            str1+=word1[i]
            str1+=word2[j]
            i+=1
            j+=1
            n1-=1
            n2-=1
        if n1==0:
            str1+=word2[j:]
        if n2==0:
            str1+=word1[i:]
        return str1
            
            
            

        