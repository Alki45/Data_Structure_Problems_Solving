class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        max_=0
        piles.sort()
        n=len(piles)
        for i in range(n//3,n,2):
            max_+=piles[i]
        return max_
        

        