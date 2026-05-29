class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum=2**31-1
        for num in nums:
            Sum=0
            while num !=0:
                digit=num%10
                Sum+=digit
                num=num//10

            minimum=min(minimum,Sum)

        return minimum


        