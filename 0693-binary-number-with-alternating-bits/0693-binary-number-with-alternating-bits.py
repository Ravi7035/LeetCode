class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary_string=bin(n)[2:]
        left=0
        right=1

        while right < len(binary_string):

            if binary_string[left]==binary_string[right]:

                return False

            left+=1
            right+=1
        return True
        
     

        



        

