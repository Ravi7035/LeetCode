class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        m=len(grid)
        n=len(grid[0])
        Total_sum=0

        frequency={}
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] not in frequency:
                    frequency[grid[i][j]]=1
                else:
                    frequency[grid[i][j]]+=1

                Total_sum+=grid[i][j]

        for num in frequency:
            if frequency[num] >1:
                ans.append(num)
        size=n*n
        Sum=(size*(size+1))//2

        ans.append(Sum-Total_sum+ans[0])

        return ans

        
        