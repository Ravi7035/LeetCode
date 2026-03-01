class Solution(object):
    def letterCombinations(self, digits):
        number_strings={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        result=[]

        def backtrack(index,current_string):
            if len(current_string)==len(digits):
                result.append(current_string)
                return 

            letters=number_strings[digits[index]]

            for letter in letters:
                backtrack(index+1,current_string+letter)
      
        backtrack(0,"")

        return result