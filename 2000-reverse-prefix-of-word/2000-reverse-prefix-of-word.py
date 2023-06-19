class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch  not in word:
            return word
        x=word.index(ch)
        print(x)
        s=word[:x+1]
        res=s[::-1]+word[x+1:]
        return res

        