class Solution:
    def frequencySort(self, s: str) -> str:
        output=[]
        for i in set(s):
            count=s.count(i)
            output.append(i*count)
        x=sorted(output,reverse=True,key=len)
        
        return "".join(x)
    # return "".join(sorted(sorted(s),reverse=1,key=s.count))

        