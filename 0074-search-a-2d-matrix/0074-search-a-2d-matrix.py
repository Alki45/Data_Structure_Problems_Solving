class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1

        while start <= end:
            mid = (start + end) // 2
            row, col = mid // cols, mid % cols
            current = matrix[row][col]

            if current == target:
                return True

            if current < target:
                start = mid + 1
            else:
                end = mid - 1

        return False