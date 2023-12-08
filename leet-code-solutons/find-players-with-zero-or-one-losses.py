class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = collections.Counter()
        players = set() # to catch all the players without any repetitions
        
        for winner, loser in matches:
            losses[loser] += 1
            players.add(winner)
            players.add(loser)
        
        no_losses, one_loss = [], []
        
        for player in players:
            if losses[player] == 0:
                no_losses.append(player) # collect players without any losses
            elif losses[player] == 1:
                one_loss.append(player) # collect players with only one loss
        
        return [sorted(no_losses), sorted(one_loss)]

        