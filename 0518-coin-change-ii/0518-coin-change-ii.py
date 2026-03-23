class Solution(object):
    def change(self, amount, coins):
        #memoization method 
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def solve(index,target):
            if target==0:
                return 1

            if index <0:
                return 0

            if dp[index][target] != -1:
                return dp[index][target]

            not_take=solve(index-1,target)

            take=0

            if coins[index] <= target:

                take=solve(index,target-coins[index])

            dp[index][target]=not_take+take

            return dp[index][target]

        return solve(len(coins)-1,amount)
       