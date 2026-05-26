class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        hash_table={}
        count=0
        for i in range(len(word)):
            if word[i].isupper():
                continue

            if word[i] not in hash_table:
                hash_table[word[i]]=1
            
            else:
                continue
            
            if word[i].upper() in word:
                count+=1

        return count

            

            

        

        