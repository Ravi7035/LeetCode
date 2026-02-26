class Solution(object):
    def permute(self, nums):
        
        result=[]

        def Permutation(path,remaining):
            #base case..if no elements left in remaining paths append the path and return 
            if not remaining:
                result.append(path)
                return 

            for i in range(len(remaining)):

                Permutation(path+[remaining[i]],remaining[:i]+remaining[i+1:])

        Permutation([],nums)

        return result



           
        
        


      
        

      
        