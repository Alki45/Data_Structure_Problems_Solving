class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)
        col = len(dungeon[0])

        dp = [[inf] * (col + 1) for _ in range (row+1)]

        dp [row][col-1] = dp[row-1][col] = 1
        
        for i in range (row - 1, -1,-1):
            for j in range(col -1, -1, -1):
                min_health = min (dp[i][j+1], dp[i+1][j])
                dp[i][j] = max(1, min_health -dungeon[i][j])
        return dp[0][0]



