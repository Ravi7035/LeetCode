class Solution(object):
    def maximumTotalDamage(self, power):

        freq={}

        for num in power:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num]+=1

        values=sorted(freq.keys())
        n=len(values)
        dp=[-1]*(n+1)

        def solve(index):

            if index >= n:
                return 0

            if dp[index]!=-1:
                return dp[index]

            not_take=0 + solve(index+1)

            power=values[index] * freq[values[index]]

            take=0
            
            j=index+1

            while j < n and values[j]<=values[index]+2:
                j+=1

            take=power + solve(j)
            
            dp[index]=max(take,not_take)
            return dp[index]
            

        return solve(0)


        