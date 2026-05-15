class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hash_map={}
       
        for i,value in enumerate(nums):

            if value in hash_map:

                return True

            else:

                hash_map[value]=i


        return False



        