class Solution(object):
    def numSteps(self, s):
        #converting the given binary number first 
        n=0
        def binary(s,n):
            for i in range(len(s)-1,-1,-1):
                n+=(2**(len(s)-i-1))*int(s[i])
            return n


        binary_number=binary(s,n)

        count=0

        while binary_number !=1:
            if binary_number%2==0:
                binary_number=binary_number//2

            else:
                binary_number+=1
                count+=1
                binary_number=binary_number//2

            count+=1

        return count

       









        