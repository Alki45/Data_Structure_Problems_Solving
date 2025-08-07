class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new_list =[ i for j in matrix for i in j ]
        new_list.sort()
        return new_list[k-1]
        