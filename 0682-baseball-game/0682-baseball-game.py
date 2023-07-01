class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        s = 0
        for op in ops:
            if op == "C":
                s -= stack.pop()
            elif op == 'D':
                stack.append(2*stack[-1])
                s += stack[-1]
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
                s += stack[-1]
            else:
                stack.append(int(op))
                s += stack[-1]
        return s
         
        