class Solution(object):
    def jump(self, nums):
        farthest=0
        current_end=0
        min_jumps=0

        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])

            if current_end==i:
                min_jumps+=1
                current_end=farthest
        return min_jumps


            
           
        

        

      
       

       



                
        
        