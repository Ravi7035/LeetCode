class Solution(object):
    def sequentialDigits(self, low, high):

        #substrings of "123456789" are the only seqeuential integers 
        #containing sequential digits
        #To get those we maintain that particular length of window and move throw 
        #entire substring then containing  the integers can be retreived

        s="123456789"

        output=[]

        LowIntegerLength=len(str(low))
        HighIntegerLength=len(str(high))


        for length in range(LowIntegerLength,HighIntegerLength+1):
            for i in range(10-length):
                number=int(s[i:i+length])
                if low <= number <=  high:
                    output.append(number)

        return output

            

        

     