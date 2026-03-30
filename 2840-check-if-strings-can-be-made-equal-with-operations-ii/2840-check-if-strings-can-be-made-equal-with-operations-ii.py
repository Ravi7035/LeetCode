class Solution(object):
    def checkStrings(self, s1, s2):
        from collections import Counter

        if Counter(s1[::2])==Counter(s2[::2]) and Counter(s1[1::2])==Counter(s2[1::2]):

            return True

        else:

            return False





         

        
        