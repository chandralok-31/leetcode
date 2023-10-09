class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = list(Counter(word).values())
        if len(set(freq)) > 2: return False
        for i in range(len(freq)):
            freq[i] -= 1
            len_ = len(set(freq))
            if len_ == 1 or (len_ == 2 and freq[i] == 0):
                return True
            freq[i] += 1
        return False
        