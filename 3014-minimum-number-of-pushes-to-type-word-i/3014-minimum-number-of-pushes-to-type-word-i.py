class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        #As the brute is possible through iterating over constant number of keys 
        #and constant number of letters of 26 and iterating over mapping of the 
        #constant 9 keys mapped to the random letters,itself costs a constant run 
        #time(o(constant) time complexity)
        maximum=0
        Total_Cost=0
        for ch in word:
            maximum+=1

            if maximum <=8:
                Total_Cost+=1
            elif maximum <= 16:
                Total_Cost+=2
            elif maximum <= 24:
                Total_Cost+=3
            else:
                Total_Cost+=4

        return Total_Cost
                
        