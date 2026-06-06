class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #prefix sum
        Total_sum=0
        prefix_sum=[]
        for i in range(len(nums)):
            if i==0:
                prefix_sum.append(0)
            else:
                Total_sum+=nums[i-1]
                prefix_sum.append(Total_sum)

        #suffix sum
        Total_sum=0
        suffix_sum=[]

        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                suffix_sum.append(0)
            else:
                Total_sum+=nums[i+1]
                suffix_sum.append(Total_sum)

        suffix_sum.reverse()

        #output block
        ans=[]
        for i in range(len(nums)):
            ans.append(abs(prefix_sum[i]-suffix_sum[i]))


        return ans
                
            
        