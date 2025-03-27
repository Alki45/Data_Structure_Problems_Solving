from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners=[winer[0] for winer in matches]
        losers=[loser[1] for loser in matches]
        loser_dict=Counter(losers)
        result=[sorted(list((set(winners)-set(losers)))),sorted([key for key,value in loser_dict.items() if value==1])]
        return result