class Solution(object):
    def isPowerOfTwo(self, n):
        
        def ispower(n):

            if n==1:
                return True
            elif n<=0 or n%2 != 0:

                return False

            return ispower(n//2)

        return ispower(n)

        
      
        
        
             