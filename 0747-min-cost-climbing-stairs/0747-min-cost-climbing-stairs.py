class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        curr = 0
        prev = 0
        prev2 = 0
                    
        for i in reversed(range(0, len(cost))):
            prev2 = prev
            prev = curr
            curr = cost[i] + min(prev, prev2)
        
        return min(curr, prev)
        