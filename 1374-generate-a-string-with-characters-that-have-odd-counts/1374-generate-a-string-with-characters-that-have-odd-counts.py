class Solution:
    def generateTheString(self, n: int) -> str:
        str1=""
        if n==1:
            str1+='a'
        elif n==2:
            str1+='a'
            str1+='b'
        elif n%2==0:
            str1+='a'*(n-1)
            str1+='b'
        else:
            str1+='a'*(n-2)
            str1+='b'
            str1+='c'
        return str1
        