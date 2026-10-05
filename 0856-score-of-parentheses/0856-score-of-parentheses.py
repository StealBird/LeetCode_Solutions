class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                inner = stack.pop()


                if inner == 0:
                    score = 1

                else :
                    score = 2 * inner

                stack[-1] += score

        return stack[0]
        