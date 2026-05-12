class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st=set(nums)
        longest=0

        for num in nums:
            
            if num-1 not  in st:

                curr=num
                length=1

                while curr+1 in st:
                    curr+=1
                    length+=1

                longest=max(longest,length)

        return longest

        