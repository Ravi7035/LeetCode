class Solution(object):
    def constructProductMatrix(self, grid):
        m=len(grid)
        n=len(grid[0])
        
        #flattent the 2d array to 1d 
        arr=[]
        for row in grid:
            arr.extend(row)
        size=len(arr)

        #prefix product
        prefix=[1]*size
        for i in range(1,size):
            prefix[i]=(prefix[i-1] * arr[i-1]) %12345

        #suffix_product
        suffix=[1]*size
        for i in range(size-2,-1,-1):
            suffix[i]=(suffix[i+1] * arr[i+1])%12345

        #build the matrix

        res = [[0]*n for _ in range(m)]
        
        for i in range(size):
            val = (prefix[i] * suffix[i]) % 12345
            r, c = i // n, i % n
            res[r][c] = val

        return res

        
        

                
        
            
                  