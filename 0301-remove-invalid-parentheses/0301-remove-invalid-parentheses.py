class Solution(object):
    def removeInvalidParentheses(self, s):
        res=set()
        #calculating how many invalid ones are there
        left_removal=right_removal=0
        for ch in s:
            if ch=="(":
                left_removal+=1
            elif ch==")":
                if left_removal >0:
                    left_removal-=1
                else:
                    right_removal+=1

        def backtrack(index,left_removal,right_removal,path,balance):
            if index==len(s):
                if balance==0 and left_removal==0 and right_removal==0:
                    res.add(path)
                return 

            ch=s[index]

            if  ch=="(" and left_removal >0:
                backtrack(index+1,left_removal-1,right_removal,path,balance)
            elif ch==")" and right_removal >0:
                backtrack(index+1,left_removal,right_removal-1,path,balance)

            if ch not in "()":
                backtrack(index+1,left_removal,right_removal,path+ch,balance)
            elif ch=="(":
                backtrack(index+1,left_removal,right_removal,path+ch,balance+1)
            elif ch==")" and balance >0:
                backtrack(index+1,left_removal,right_removal,path+ch,balance-1)

        backtrack(0,left_removal,right_removal,"",0)

        return sorted(res)

            


        
                
                
                
      