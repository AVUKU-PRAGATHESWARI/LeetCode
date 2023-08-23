class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        dp = [0]*(1+max(ages))
        score_age = sorted(zip(scores, ages))
        for score, age in score_age:
            dp[age] = score + max(dp[:age+1])
        return max(dp)
        