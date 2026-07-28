class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        #As the lexicographically smallest one depends upon the smallest left half
        #to generate it, includes by rearranging as smallest as possible 
        #through checking the count of each character. If any character with odd
        #then middle character will be present else not required or should not #contain it.

        #Reversing function to get the palindrome works well


        #Counting of each character
        from collections import Counter
        Freq=Counter(s)
        left=[]
        middle=""
        for ch in sorted(Freq):
            left.append(ch*(Freq[ch]//2))
            if Freq[ch] % 2 == 1:
                middle=ch

        left="".join(left)

        right=left[::-1]

        return left + middle + right


        
