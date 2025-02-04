class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count=0
        players.sort()
        trainers.sort()
        for i in range(len(players)):
            for j in range(len(trainers)):
                if(players[i]<=trainers[j]):
                    count+=1
                    trainers.remove(trainers[j])
                    break

        return count