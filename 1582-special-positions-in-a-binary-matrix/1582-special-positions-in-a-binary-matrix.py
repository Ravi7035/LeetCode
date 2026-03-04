class Solution(object):
    def numSpecial(self, mat):
        #traverse through the every row 
        rows=[]
        for row in range(len(mat)):
            count=0
            for col in range(len(mat[0])):
                if mat[row][col]==1:
                    count+=1
            rows.append(count)

        #traverse through the every column
        columns=[]
        for col in range(len(mat[0])):
            count=0
            for row in range(len(mat)):
                if mat[row][col]==1:
                    count+=1

            columns.append(count)
        output=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    if rows[i]==1 and columns[j]==1:
                        output+=1



        return output 
                        

        
            
            
            
        
                



                
        



       
        