class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_count=0
        def isprime(number):
            count=0
            for i in range(1,number+1):

                if number%i==0:

                    count+=1

            if count==2:

                return 1
            else:
                return 0

        for i in range(left,right+1):
            binary_number=bin(i)
            count_setbits=binary_number.count('1')
            prime_count+=isprime(count_setbits)

        return prime_count

            

            

            
            

            
        