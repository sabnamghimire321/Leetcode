class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for c in range(1, amount + 1):
            for coin in coins:
                if coin <= c:
                    dp[c] = min(dp[c], dp[c - coin] + 1)
                    
        return dp[amount] if dp[amount] != float('inf') else -1
