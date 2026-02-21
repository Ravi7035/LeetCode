class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
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
        """

        #optimization for this.since the range is 10**6 the maximum number of ones upto that range 
        #are 20 only.so we have to check the primes less than 21.{2,3,5,7,11,13,17,19}

        prime_count=0
        prime_numbers=[2,3,5,7,11,13,17,19]
        
        for number in range(left,right+1):
            ones=bin(number).count('1')
            if ones in prime_numbers:

                prime_count+=1

        return prime_count
            



            

            

            
            

            
        