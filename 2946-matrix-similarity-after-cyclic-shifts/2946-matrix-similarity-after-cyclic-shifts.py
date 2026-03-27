class Solution(object):
    def areSimilar(self, mat, k):
        temp_mat=[row[:] for row in mat]

        k=k%len(mat[0])

        def left_rotate(row_value):
            
            temp=mat[row_value][0]

            for i in range(len(mat[0])-1):

                mat[row_value][i]=mat[row_value][i+1]
            
            mat[row_value][-1]=temp


        def right_rotate(row_value):

            temp=mat[row_value][-1]

            for i in range(len(mat[0])-1,0,-1):

                mat[row_value][i]=mat[row_value][i-1]

            mat[row_value][0]=temp


        while k:

            for i in range(len(mat)):
                
                if i%2==0:
                    left_rotate(i)

                else:
                    right_rotate(i)

            k-=1


        if temp_mat==mat:
            
            return True

        else:
            return False

       
        