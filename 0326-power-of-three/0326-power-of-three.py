class Solution(object):
    def isPowerOfThree(self, n):
        def ispower(n):

            if n==1:
                return True

            elif n<=0 or n%3 != 0:

                return False

            return ispower(n//3)

        return ispower(n)