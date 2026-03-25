class Solution(object):
    def isMatch(self, s, p):
        m=len(s)
        n=len(p)
        dp=[[-1]*(n+1) for _ in range(m+1)]

        def solve(i,j):
            if i <0 and j <0 :
                return True
            if j < 0:
                return False
            if i < 0:
                for k in range(j+1):
                    if p[k]!="*":
                        return False

                return True

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i]==p[j] or p[j]=="?":
                dp[i][j]= solve(i-1,j-1)

            elif p[j]=="*":
                dp[i][j]=solve(i-1,j) or solve(i,j-1)

            else:
                dp[i][j]=False

            return  dp[i][j]


        return solve(m-1,n-1)


            



          