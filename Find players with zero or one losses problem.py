class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = Counter()
        for winner, loser in matches:
            losses[loser] += 1
            if winner not in losses:
                losses[winner] = 0
        never_lose = []
        lose_once = []
        for player in losses:
            if losses[player] == 0:
                never_lose.append(player)
            elif losses[player] == 1:
                lose_once.append(player)
        return [sorted(never_lose), sorted(lose_once)]
