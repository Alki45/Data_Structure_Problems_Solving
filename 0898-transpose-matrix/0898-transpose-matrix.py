class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for i in range(len(matrix[0])):
            new=[]
            for row in matrix:
                new.append(row[i])
            transposed.append(new)
        return transposed
        