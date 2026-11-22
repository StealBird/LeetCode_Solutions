class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        postfix = self.infixToPostfix(s)
        return self.evaluate(postfix)

    def evaluate(self, postfix):
        st = []
        for tok in postfix:
            if tok in ('+', '-', '*', '/', '^'):
                b = st.pop()
                a = st.pop()

                if tok == '+':
                    st.append(a + b)
                elif tok == '-':
                    st.append(a - b)
                elif tok == '*':
                    st.append(a * b)
                elif tok == '/':
                    st.append(int(a / b))
                else:
                    st.append(a ** b)
            else:
                st.append(int(tok))
        return st[0]

    def infixToPostfix(self, s: str) -> list:
        stack = []
        ans = []
        i = 0

        while i < len(s):
            char = s[i]

            if char >= '0' and char <= '9':
                num = ''
                while i < len(s) and s[i] >= '0' and s[i] <= '9':
                    num += s[i]
                    i += 1
                ans.append(num)
                continue

            elif char == '(':
                stack.append(char)

            elif char == ')':
                while stack and stack[-1] != '(':
                    ans.append(stack[-1])
                    stack.pop()
                stack.pop()

            else:
                if char == '-' and (i == 0 or s[i-1] == '('):   # NEW
                    ans.append('0')

                while stack and not (self.priority(char) > self.priority(stack[-1]) or (self.priority(char) == self.priority(stack[-1]) and char == '^')):
                    ans.append(stack[-1])
                    stack.pop()
                stack.append(char)

            i += 1

        while stack:
            ans.append(stack[-1])
            stack.pop()

        return ans

    def priority(self, operator):
        if operator == '^':
            return 3
        elif operator in ('*', '/'):
            return 2
        elif operator in ('+', '-'):
            return 1
        else:
            return -1