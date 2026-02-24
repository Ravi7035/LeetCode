class Solution(object):
    def fib(self, n):
        #F(n)=F(n-1)+F(n-2) if n > 0
        #if n=0 F(n) equal to zero
        #if n=1 F(n) equal to 1

        def fibonacci(n):
            if n ==0:
                return 0
            elif n==1:
                return 1

            return fibonacci(n-1)+fibonacci(n-2)

        return fibonacci(n)

        