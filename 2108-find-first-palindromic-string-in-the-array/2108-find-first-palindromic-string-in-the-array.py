class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palindromic(s):
            if s==s[::-1]:
                return True 
            else:
                return False
        str1=""
        for i in words:
            if palindromic(i):
                str1+=i
                return str1
        return str1

        