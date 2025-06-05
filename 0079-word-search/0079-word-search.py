from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.backtrack(i, j, 0):
                    return True
        return False

    def backtrack(self, i: int, j: int, k: int) -> bool:
        if k == len(self.word):
            return True
        if (
            i < 0 or i >= self.rows or
            j < 0 or j >= self.cols or
            self.board[i][j] != self.word[k]
        ):
            return False

        temp = self.board[i][j]
        self.board[i][j] = '#'  # mark as visited

        found = (
            self.backtrack(i+1, j, k+1) or
            self.backtrack(i-1, j, k+1) or
            self.backtrack(i, j+1, k+1) or
            self.backtrack(i, j-1, k+1)
        )

        self.board[i][j] = temp  # restore original letter
        return found
