class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while top<bottom and left<right:
            for i in range(right-left):
                temp = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = temp
            top += 1
            bottom -= 1
            left += 1
            right -= 1