class Solution(object):
    def minFlips(self, s):
        #instead of manually rotation of array we use 2x string and sliding window
        s=s+s
        alt1=""
        alt2=""
        minimum_operations=2**31-1
        for i in range(len(s)):
            if i%2:
                alt1+="1"
                alt2+="0"
            else:
                alt1+="0"
                alt2+="1"
        diff1=diff2=0
        l=0
        for r in range(len(s)):
            if s[r]!=alt1[r]:
                diff1+=1
            if s[r]!=alt2[r]:
                diff2+=1
            
            if r-l+1>len(s)//2:
                if s[l]!=alt1[l]:
                    diff1-=1
                if s[l]!=alt2[l]:
                    diff2-=1
                l+=1

            if r-l+1==len(s)//2:
                minimum_operations=min(minimum_operations,diff1,diff2)

        return minimum_operations



        

        
       
        