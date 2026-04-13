class Solution(object):
    def getMinDistance(self, nums, target, start):
        min_dist=float('inf')
        for i  in range(len(nums)):
            if nums[i]==target:
                if abs(i-start) < min_dist:
                    min_dist=abs(i-start)

        return min_dist



      