class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] in seen:
                    return False
                elif board[row][i] != '.':
                    seen.add(board[row][i])

            
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] in seen:
                    return False
                elif board[i][col] != '.':
                    seen.add(board[i][col])


# 0, 1, 2 -> 0
# 3, 4, 5 -> 1
# 6, 7, 8 -> 3
        for box in range(9): # 0, 1, 2, 3
            seen = set()
            for i in range(3 * (box // 3), 3 * (box // 3) + 3): # 0, 1, 3, 0..3, 0..3
                for j in range((box % 3) * 3, (box % 3) * 3 + 3): # 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5
                    if board[i][j] in seen:
                        return False
                    elif board[i][j] != '.':
                        seen.add(board[i][j])



        return True





        