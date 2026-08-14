class Solution(object):
    def maximumLengthSubstring(self, s):

        hash_table={}
        left=0
        max_length=0
    
        for right in range(len(s)):

            if s[right] not in hash_table:
                hash_table[s[right]]=1
            else:
                hash_table[s[right]]+=1

            
            while hash_table[s[right]] > 2:
                hash_table[s[left]]-=1
                left+=1

            length=right-left+1
            max_length=max(length,max_length)

        return max_length

                

     