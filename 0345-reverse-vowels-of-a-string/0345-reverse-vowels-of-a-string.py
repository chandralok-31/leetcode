class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=[]
        d={'a', 'e', 'i', 'o','u','A','E','I','O','U'}
        s=list(s)
        for i in range(len(s)):
            if s[i] in d:
                arr.append(s[i])
                s[i]="$"
        for i in range(len(s)):
            if s[i]=="$":
                s[i]=arr.pop(-1)
        return "".join(s)
        