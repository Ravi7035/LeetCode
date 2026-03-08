class Solution(object):
    def findDifferentBinaryString(self, nums):
        strings={}
        output=[]
        for string in nums:
            strings[string]=strings.get(string,0)+1

        def backtrack(n,path):

            if output:
                return 

            if len(path)==n:
                if path not in strings:
                    output.append(path[::])
                return

            backtrack(n,path+"0")
            backtrack(n,path+"1")

        backtrack(len(nums),"")

        return output[0]

        



       
        