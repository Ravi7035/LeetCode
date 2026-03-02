class Solution(object):
    def getHappyString(self, n, k):
        letter_table={
            1:"a",
            2:"b",
            3:"c"
        }
        result=[]
        def backtrack(index,current_string):
            if len(current_string)==n:
                result.append(current_string)
                return 

            for i in  range(1,len(letter_table)+1):
                if current_string and  (current_string[-1]==letter_table[i]):
                    continue
                backtrack(index+1,current_string+letter_table[i])

        backtrack(1,"")

        return result[k-1] if len(result) >= k else ""

        
        
            
        
       