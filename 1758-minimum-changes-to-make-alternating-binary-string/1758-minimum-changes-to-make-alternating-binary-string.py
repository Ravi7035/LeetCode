class Solution(object):
    def minOperations(self, s):
        """
       #doing for 0's 
        alt=0
        min_operations_zeroes=0
        for i in range(len(s)):
            if s[i]==str(alt):
                alt=1 if alt==0 else 0
                continue
            min_operations_zeroes+=1
            alt=0 if alt ==1 else 1 
        #doing for 1's
        alt=1
        min_operations_ones=0
        for i in range(len(s)):
            if s[i]==str(alt):
                alt=0 if alt==1 else 1
                continue
            min_operations_ones+=1
            alt=1 if alt==0 else 0

        return min(min_operations_ones,min_operations_zeroes)
        """

        #optimized and single pass solution 
        mismatches=0
        for i in range(len(s)):
            expected=str(i%2)

            if s[i]!=expected:
                mismatches+=1

        return min(mismatches,len(s)-mismatches) #since if mismatches the first pattern its automatically falls on second pattern
        




        