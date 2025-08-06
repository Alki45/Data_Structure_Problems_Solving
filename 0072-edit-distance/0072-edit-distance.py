class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row = len(word1)
        col = len(word2)
        dp = [ [0] * (col +1) for _ in range(row +1) ]


        for i in range ( row+1):
            dp[i][col] = row - i
        for j in range (col+1):
            dp[row][j] = col - j

        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1+ min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])         
        return dp[0][0]
        
        