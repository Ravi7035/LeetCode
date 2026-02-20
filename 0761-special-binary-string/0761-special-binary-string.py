class Solution(object):
    def makeLargestSpecial(self, s):
        if len(s)<=2:
            return s
        count=0
        start=0
        blocks=[]

        for i in range(len(s)):

            if s[i]=="1":
                count+=1
            else:
                count-=1

            if count==0:
                innerLargest=self.makeLargestSpecial(s[start+1:i])
                blocks.append("1"+innerLargest+"0")
                start=i+1
                
            
        blocks.sort(reverse=True)

        return "".join(blocks)


       
        