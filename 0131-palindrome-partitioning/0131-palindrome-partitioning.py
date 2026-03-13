class Solution(object):
    def partition(self, s):
        paths=[]
        def isPalindrome(l,r):
            while l <r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1

            return True

        def backtrack(start,path):
            if start==len(s):
                paths.append(path[:])

            for i in range(start,len(s)):
                if isPalindrome(start,i):
                    path.append(s[start:i+1])
                    backtrack(i+1,path)
                    path.pop()

        backtrack(0,[])
        return paths 
                
            

        