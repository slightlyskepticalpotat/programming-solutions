class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif char == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()
            elif char == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
        return stack == []
