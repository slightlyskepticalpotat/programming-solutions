class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans, tokens = [], [int(i) if i not in "+-*/" else i for i in tokens]
        for i in tokens:
            if i == "+":
                ans.append(ans.pop() + ans.pop())
            elif i == "-":
                ans.append(-ans.pop() + ans.pop())
            elif i == "*":
                ans.append(ans.pop() * ans.pop())
            elif i == "/":
                ans.append(int(1 / ans.pop() * ans.pop()))
            else:
                ans.append(i)
        return ans[0]