class Solution(object):
    def combinationSum3(self, k, n):
        output=[]
        def backtrack(start,remaining,path):
            
            if remaining==0 and len(path)==k:
                output.append(path[::])
                return 
            if len(path)>k:
                return
            if remaining<0:
                return 

            for number in range(start,10):
                path.append(number)
                backtrack(number+1,remaining-number,path)
                path.pop()

        backtrack(1,n,[])

        return output                
       
        