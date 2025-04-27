class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle_lists=[i for i in range(1,n+1)]
        index=0
        while len(circle_lists)>1:

            removed_index = (index+k-1)%len(circle_lists)

            circle_lists.pop(removed_index)
            index=removed_index
        return circle_lists[0]
        