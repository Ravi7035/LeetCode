class Solution(object):
    def isPowerOfFour(self, n):
        def power(n):

            if n==1:
                return True
            
            elif n <=0 or n%4!=0:

                return False

            return power(n//4)

        return power(n)
        