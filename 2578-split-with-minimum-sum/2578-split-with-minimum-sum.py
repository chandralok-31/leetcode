class Solution:
    def splitNum(self, num: int) -> int:
        x=list(str(num))
        x.sort()

        num1=""
        num2=""
        for i in range(len(x)):
            if i%2==0:
                num1+=x[i]
            else:
                num2+=x[i]
        return int(num1)+int(num2)
        