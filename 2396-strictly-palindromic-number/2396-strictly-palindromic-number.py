class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert_to_base(num,base):
            if num==0:
                return 0
            result=""
            while num>0:
                num,remainder=divmod(num,base)
                result=str(remainder)+result
            return result
        
        for i in range(2,n-1):
            x=convert_to_base(n,i)
            if x!=x[::-1]:
                return False
        return True
                
        