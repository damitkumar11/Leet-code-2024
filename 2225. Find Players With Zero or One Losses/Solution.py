from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners = set()
        losers_count = defaultdict(int)

        for match in matches:
            winner, loser = match
            winners.add(winner)
            losers_count[loser] += 1

        not_lost = [player for player in winners if losers_count[player] == 0]
        lost_once = [player for player in losers_count if losers_count[player] == 1]

        return [sorted(not_lost), sorted(lost_once)]
