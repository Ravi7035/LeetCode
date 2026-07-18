class Solution(object):
    def findGCD(self, nums):
        from fractions import gcd
        nums.sort()
        return gcd(nums[0],nums[-1])


        