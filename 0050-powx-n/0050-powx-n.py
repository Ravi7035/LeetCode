class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        # return x**n

        #recursion in o(N) approach
        """

        def power(x,n):

            if n==0:

                return 1

            x=x*power(x,n-1)

            return x

        return power(x,n)
        """
    

        def power(x,n):

            if n==0:

                return 1

            if n < 0:

                return 1/power(x,-n)

            half=power(x,n//2)

            if n%2==0:

                return half*half

            else:
                return x*half*half

        return power(x,n)



       
       
     