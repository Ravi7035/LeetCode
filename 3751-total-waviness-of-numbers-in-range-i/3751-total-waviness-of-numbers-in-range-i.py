class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        waviness=0
        for i in range(num1,num2+1):
            number=str(i)
            for digit in range(1,len(number)-1):
                if (int(number[digit]) > int(number[digit+1]) and int(number[digit]) > int(number[digit-1]) ) or int(number[digit]) < int(number[digit-1]) and int(number[digit]) < int(number[digit+1]):
                    waviness+=1

        return waviness
            
            
        