class Solution(object):
    def predictTheWinner(self, nums):

        def theWinner(l,r):

            if l==r:
                return nums[l]

            pick_left=nums[l]-theWinner(l+1,r)
            pick_right=nums[r]-theWinner(l,r-1)

            return max(pick_left,pick_right)

        return theWinner(0,len(nums)-1)>=0

        
        