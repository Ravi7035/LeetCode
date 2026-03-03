class Solution(object):
    def numsSameConsecDiff(self, n, k):
        result=[]
        def backtrack(number,length):
            if n==length:
                result.append(number)
                return 

            last_digit=number%10

            for digit in {last_digit+k,last_digit-k}:
                if 0<=digit <=9:
                    backtrack(number*10+digit,length+1)
        for start in range(1,10):
            backtrack(start,1)
        
        return result
        





        