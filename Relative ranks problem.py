class Solution:
    from collections import Counter
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {}
        sorted_score = sorted(score, reverse=True)
        for i , v in enumerate(sorted_score):
            if i == 0 :
                rank[v]="Gold Medal"
            elif i == 1 :
                rank[v]="Silver Medal"
            elif i == 2 :
                rank[v]= "Bronze Medal"
            else:
                rank[v]=str(i+1)
        return [rank[s] for s in score]
