class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        curr = []
        def backtrack(start, end):
            if len(curr) == 2 * n:
                out.append("".join(curr))
                return
            if start < n:
                curr.append("(")
                backtrack(start + 1, end)
                curr.pop()
            if end < start:
                curr.append(")")
                backtrack(start, end + 1)
                curr.pop()
        backtrack(0, 0)
        return out
                    