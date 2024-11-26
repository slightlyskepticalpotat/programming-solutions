class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players, idx = [i for i in range(1, n + 1)], 0
        while len(players) > 1:
            idx = (idx + k - 1) % len(players)
            players.pop(idx)
        return players[0]