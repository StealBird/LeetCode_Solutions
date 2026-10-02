class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        self.generate("", n, ans)
        return ans

    def generate(self, curr: str, n: int, ans: list[str]) -> None:

        if len(curr) == 2*n:
            if self.isValid(curr):
                ans.append(curr)

            return

        self.generate(curr + "(", n, ans)

        self.generate(curr + ")", n, ans)
        
    def isValid(self, s: str) -> bool:
        balanced = 0

        for ch in s:
            if ch == '(':
                balanced += 1
            else:
                balanced -= 1

            if balanced < 0:
                return False

        return balanced == 0