class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # convert wordDict to a set for constant time lookup
        n = len(s)
        dp = [False] * (n+1)  # create an array dp of length n+1
        dp[0] = True  # empty string can be segmented into an empty sequence of words

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
        