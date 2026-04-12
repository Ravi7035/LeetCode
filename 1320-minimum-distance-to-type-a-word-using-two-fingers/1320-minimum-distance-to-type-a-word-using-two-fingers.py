class Solution(object):
    def minimumDistance(self, word):

        n=len(word)

        dp=[[[-1]*27 for _ in range(27)] for _ in range(n+1)]

       
        def get_index(x):

            if x==-1:
                return 26

            return ord(x)-ord('A')


        def pos(x):
            if x==-1:
                return (0,0)
            v=ord(x)-ord('A')
            return (v // 6 ,v % 6)

        def dist(a,b):
            if a==-1:
                return 0
            x1,y1=pos(a)
            x2,y2=pos(b)

            return abs(x1-x2) + abs(y1-y2)

        def solve(index,f1_pos,f2_pos):


            if index==n:

                return 0

            i=get_index(f1_pos)
            j=get_index(f2_pos)

            if dp[index][i][j]!=-1:

                return dp[index][i][j]

            #finger_one

            cost1=dist(f1_pos,word[index])+solve(index+1,word[index],f2_pos)

            #finger_two

            cost2=dist(f2_pos,word[index])+solve(index+1,f1_pos,word[index])


            dp[index][i][j]=min(cost1,cost2)

            return dp[index][i][j]


        return solve(0,-1,-1)

     
        