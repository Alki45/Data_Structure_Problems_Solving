class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        dp =[[inf] * (col) for _ in range(row)]
        for cols in range(col):
            dp[row -1][cols] = matrix[row-1][cols]
        print(dp)
        for i in range (row -2,-1,-1):
            for j in range (col):
                down = dp[i + 1][j]
                down_left = dp[i+1][j-1] if j - 1 >= 0 else inf
                down_right = dp[i+1][j+1] if j + 1 < col else inf

                dp[i][j] =  matrix[i][j] + min(down,down_left,down_right)
        return min(dp[0])



        