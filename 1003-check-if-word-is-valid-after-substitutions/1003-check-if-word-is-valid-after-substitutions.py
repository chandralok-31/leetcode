class Solution:
    def isValid(self, s: str) -> bool:
        while ("abc" in s):
                s=s.replace("abc","")
        return s==""
                
#         n=len(s)
#         if n%3!=0:
#             return False
#         elif n==3 and s=="abc":
#             return True
#         else:
#             x=n//3

#         for i in range(n-3):
#             print(s[:i]+s[i+3:])
#             if s[i:i+3]=="abc" and s[:i]+s[i+3:]==("abc")*(x-1):
#                 return True
#         return False
       
        
        