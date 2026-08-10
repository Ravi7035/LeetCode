class Solution(object):
    def winnerSquareGame(self, n):

        dp = [-1] * (n + 1)

        def solve(n):
            if n == 0:
                return False

            if dp[n] != -1:
                return dp[n]

            i = 1

            while i * i <= n:

                # If we can leave the opponent
                # in a losing state, we win
                if solve(n - i * i) == False:
                    dp[n] = True
                    return True

                i += 1

            dp[n] = False
            return False

        return solve(n)

       
        