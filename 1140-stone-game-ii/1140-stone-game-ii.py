class Solution(object):
    def stoneGameII(self, piles):

        
        n=len(piles)
        dp=[[-1]* (n+1) for _ in range(n+1)]

        suffix=[0]*(n+1)

        for i in range(n-1,-1,-1):
            suffix[i]=suffix[i+1]+piles[i]

        def solve(index,Maximum_piles):

            n=len(piles)

            if index >= n:
                return 0

            if dp[index][Maximum_piles] != -1:
                return dp[index][Maximum_piles]
 
            best=0

            for x in range(1,2*Maximum_piles+1):

                if x + index > n:
                    break
                
                opponent=solve(index+x,max(Maximum_piles,x))

                current=suffix[index]-opponent

                best=max(best,current)

            dp[index][Maximum_piles]=best

            return dp[index][Maximum_piles]

        return solve(0,1)



                

                

                
        
        