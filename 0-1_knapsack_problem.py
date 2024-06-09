class Solution:
    def knapSack(self, W, wt, val, n): 
        if n == 0 or W == 0: 
            return 0

        if wt[n-1] > W: 
            return self.knapSack(W, wt, val, n-1)
        else: 
            return max(
                val[n-1] + self.knapSack(W-wt[n-1], wt, val, n-1), 
                self.knapSack(W, wt, val, n-1)
            )

solution = Solution()
profit = [60, 100, 120] 
weight = [10, 20, 30] 
W = 50
n = len(profit) 
print(solution.knapSack(W, weight, profit, n))
