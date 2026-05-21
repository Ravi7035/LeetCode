class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):

        # #gaining the possible pairs from arr1 and arr2

        # pairs=[]

        # for i in range(len(arr1)):
        #     for j in range(len(arr2)):

        #         pairs.append((arr1[i],arr2[j]))

        # #checking for the longest common prefix 
        # longest_prefix=0
        # for pair in pairs:
        #     ele_1,ele_2=pair

        #     ele_1=str(ele_1)
        #     ele_2=str(ele_2)

        #     i=0

        #     length=0

        #     while i < len(ele_1):
        #         if ele_1[i]==ele_2[i]:
        #             length+=1
        #             i+=1
        #         else:
        #             break
            

        #     longest_prefix=max(length,longest_prefix)


        # return longest_prefix

        #adding every possible prefix of each element into prefix hash map
        prefix={}
        for ele in arr1:
            ele=str(ele)
            for i in range(len(ele)):
                prefix[ele[:i+1]]=1

        #checking with each possible prefix of each element in the arr2 in prefix hash map
        longest_prefix=0
        for ele in arr2:
            ele=str(ele)
            for i in range(len(ele)):
                if ele[:i+1] in prefix:
                    longest_prefix=max(longest_prefix,len(ele[:i+1]))

        return longest_prefix



        


        






        
       
        