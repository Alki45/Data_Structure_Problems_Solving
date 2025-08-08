class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        dp = [0] * (n+1)

        for i in range (n-1, -1, -1):
            point, brainpower = questions[i]
            skip =dp[i+1]
            if i + brainpower +1 < n+1 :
                solve = point + dp[i + brainpower +1]
            else:
                solve = point

            dp[i] = max(skip,solve)
        return dp[0]