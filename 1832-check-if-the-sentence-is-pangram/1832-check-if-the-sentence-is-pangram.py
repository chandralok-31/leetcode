class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr=[]
        for i in sentence:
            if i not in arr:
                arr.append(i)
                
        return len(arr)==26
        