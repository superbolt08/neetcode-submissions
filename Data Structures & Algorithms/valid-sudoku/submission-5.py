class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = len(board[0])

        for row in board:
            nums = [x for x in row if x != '.']
            if len(nums) != len(set(nums)):
                return False

        for c in range(9):
            col = [board[r][c] for r in range(9) if board[r][c] != '.']
            if len(col) != len(set(col)):
                return False        

        for box_row in range(3):
            for box_col in range(3):
                box = []
                for r in range(box_row * 3, box_row * 3 + 3):
                    for c in range(box_col * 3, box_col * 3 + 3):
                        if board[r][c] != '.':
                            box.append(board[r][c])
                if len(box) != len(set(box)):
                    return False

        return True
   

  
