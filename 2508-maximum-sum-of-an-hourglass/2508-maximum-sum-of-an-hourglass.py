class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        """
        n,m=row,col
        
        """
        Max_sum=0
        n,m=len(grid),len(grid[0])
        for r in range(1,n-1):
            for c in range(1,m-1):
                summ=grid[r][c]+grid[r-1][c-1] +grid[r-1][c]+grid[r-1][c+1]+grid[r+1][c-1]+grid[r+1][c]+grid[r+1][c+1]
                Max_sum=max(Max_sum,summ)
        return Max_sum


