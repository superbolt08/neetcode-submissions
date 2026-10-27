class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, cols = len(board), len(board[0])
        def backtrack(i, j, word_mutable):
            if not word_mutable:
                return True
            if (i, j) in visited:
                return False
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if board[i][j] != word_mutable[0]:
                return False
            visited.add((i,j))
            found = (
                backtrack(i - 1, j, word_mutable[1:]) or
                backtrack(i + 1, j, word_mutable[1:]) or
                backtrack(i, j - 1, word_mutable[1:]) or
                backtrack(i, j + 1, word_mutable[1:])
            )

            visited.remove((i, j))
            return found
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, word):
                    return True
        return False