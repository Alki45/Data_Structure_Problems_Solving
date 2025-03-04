class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_pil=0
        piles.sort()
        for i in range(len(piles)//3,len(piles),2):
            max_pil+=piles[i]
        return max_pil