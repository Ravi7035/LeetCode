from fractions import gcd

class Solution(object):
    def gcdOfOddEvenSums(self, n):
        even_sum = n* (n+1)
        odd_sum =  n**2

        return gcd(even_sum,odd_sum)


       