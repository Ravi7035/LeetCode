class Solution(object):
    def minSwaps(self, grid):
        n=len(grid)

                
        #finding the trailing_zeroes in each row
        trailing_zeroes=[]
        for row in grid:
            count=0

            for x in reversed(row):
                if x ==0:
                    count+=1
                else:
                    break
            trailing_zeroes.append(count)

        #through greedy swap the rows 

        swaps=0

        for i in range(len(grid)):
            required=n-i-1
            j=i

            while j < n and trailing_zeroes[j]<required:
                j+=1

            #if every row not have enough zereos

            if j==n:
                return -1

            #swapping 

            while j >i:
                trailing_zeroes[j],trailing_zeroes[j-1]=trailing_zeroes[j-1],trailing_zeroes[j]
                swaps+=1
                j-=1


        return swaps
        

        


            
            

        



        






       
        