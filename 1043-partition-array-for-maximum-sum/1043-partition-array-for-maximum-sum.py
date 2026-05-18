class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n=len(arr)
        dp=[-1]*(n)
        INT_MIN=-2**31
        def solve(i):

            if i==n:
                return 0

            if dp[i] !=-1:
                return dp[i]

            current_max=0
            maximum=INT_MIN
            for j in range(i,min(i+k,n)):

                current_max=max(current_max,arr[j])

                length=j-i+1

                total_cost=current_max*length+solve(j+1)

                maximum=max(maximum,total_cost)


            dp[i]=maximum

            return dp[i]


        return solve(0)

            

        