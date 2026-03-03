class Solution(object):
    def subsets(self, nums):
        #the intuitive is to know what to take and what to skip
        result=[]
        def backtrack(start,path):
            result.append(path[::])

            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])

        return result


       