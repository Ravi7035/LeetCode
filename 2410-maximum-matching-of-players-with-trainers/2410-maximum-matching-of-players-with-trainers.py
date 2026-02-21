class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        output=0
        i=j=0

        while i < len(players) and j < len(trainers):
            
            if players[i] <= trainers[j]:
                output+=1
                i+=1
                j+=1
            else:
                j+=1

        return output

     
        