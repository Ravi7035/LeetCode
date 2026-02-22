class Solution(object):
    def scoreDifference(self, nums):
        player1_score=0
        player2_score=0
        turn=1

        for i,n in enumerate(nums):

            if nums[i]%2!=0:
                turn=2 if turn==1 else 1

            if (i+1)%6==0:
                turn=2 if turn==1 else 1

            if turn==1:
                player1_score+=nums[i]
            else:
                player2_score+=nums[i]
          
        return player1_score-player2_score

               
           

                

       