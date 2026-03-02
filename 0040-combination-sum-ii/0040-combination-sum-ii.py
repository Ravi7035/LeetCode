class Solution(object):
    def combinationSum2(self, candidates, target):
        output=[]
        candidates.sort()
        def backtrack(start,remaining,path):
            if remaining==0:
                output.append(path[::])
                return 
            if remaining<0:
                return

            for index in range(start,len(candidates)):
                if index > start and candidates[index]==candidates[index-1]:
                    continue
                path.append(candidates[index])
                backtrack(index+1,remaining-candidates[index],path)
                path.pop()

        backtrack(0,target,[])

        return output
       