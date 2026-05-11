class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for n in nums:
            temp=[]
            while n !=0:
                rem=n%10
                n=n//10
                temp.append(rem)

            for i in range(len(temp)-1,-1,-1):
                ans.append(temp[i])


        return ans

        