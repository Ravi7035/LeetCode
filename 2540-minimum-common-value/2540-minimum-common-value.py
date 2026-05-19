class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # def found(curr):
            # left=0
            # right=len(nums2)-1

            # while left <= right:

            #     mid=(left+right)//2

            #     if nums2[mid]==curr:
            #         return True

            #     elif nums2[mid] > curr:
            #         right-=1

            #     else:
            #         left+=1

            # return False


        # for i in range(len(nums1)):

        #     curr=nums1[i]

        #     if found(curr):

        #         return curr


        # return -1

        i=0
        j=0
        while i < len(nums1) and j < len(nums2):

            if nums1[i]==nums2[j]:
                return nums1[i]

            elif nums1[i] > nums2[j]:
                j+=1


            else:
                i+=1

        return -1

        



        