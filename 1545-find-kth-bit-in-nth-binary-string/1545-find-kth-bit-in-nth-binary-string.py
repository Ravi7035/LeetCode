class Solution(object):
    def findKthBit(self, n, k):
        def invert(current_string):
            result=""
            for char in current_string:
                if char=="1":
                    result+="0"
                else:
                    result+="1"
            return result            
                

        def reverse(current_string):
            current_list=list(current_string)
            i=0
            j=len(current_list)-1
            while i < j:
                current_list[i],current_list[j]=current_list[j],current_list[i]
                i+=1
                j-=1
            return "".join(current_list)


        def recursion(current_count,current_string):
            #base case 
            if current_count==n:
                kth_bit=current_string[k-1]
                return kth_bit

            return recursion(current_count+1,current_string+"1"+reverse(invert(current_string)))

        return recursion(1,"0")


        

        
        
     
        