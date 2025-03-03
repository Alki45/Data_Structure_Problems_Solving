class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result=[]
        max_=0
        for _ in range(len(mat)):
                result.append(mat[_].count(1))

        return [result.index(max(result)),max(result)]
        
        