class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n=len(arr)
        dp=[0]*(n+1)
        INT_MIN=-2**31

        dp[n]=0

       
        maximum=INT_MIN

        for i in range(n-1,-1,-1):
            current_max=0
            for j in range(i,min(i+k,n)):

                current_max=max(current_max,arr[j])

                length=j-i+1

                total_cost=current_max*length+dp[j+1]

                maximum=max(maximum,total_cost)


            dp[i]=maximum


        return dp[0]

            

        