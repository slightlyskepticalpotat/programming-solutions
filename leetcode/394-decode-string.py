class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, string = [], 0, ""
        for char in s:
            print(stack)
            if char == "[":
                stack.append(string)
                stack.append(num)
                string, num = "", 0
            elif char == "]":
                prev_num, prev_str = stack.pop(), stack.pop()
                string = prev_str + prev_num * string
            elif char.isdigit():
                num = num * 10 + int(char)
            else:
                string += char
        return string