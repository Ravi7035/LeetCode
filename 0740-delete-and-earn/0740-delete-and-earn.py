class Solution(object):
    def deleteAndEarn(self, nums):

        freq={}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num]+=1

        

        values=sorted(freq.keys())
        n=len(values)
        dp=[-1]*(n+1)

        def solve(index):

            if index == n:
                return 0

            if dp[index]!=-1:
                return dp[index]

            not_take=0 + solve(index+1)

            take=0

            points=values[index] * freq[values[index]]

            if index + 1 < n and values[index+1]==values[index]+1:
                take=points+solve(index+2)    

            else:
                take=points+solve(index+1)   


            dp[index]=max(take,not_take)
            return dp[index]

        return solve(0)



            

        

        
      