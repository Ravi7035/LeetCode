from fractions import gcd 
class Solution(object):
    def gcdSum(self, nums):
        n=len(nums)
        mx=[0]*n
        prefix_gcd=[]

        mx[0]=nums[0]
        for i in range(1,n):
            mx[i]=max(mx[i-1],nums[i])
        
        for i in range(n):
            prefix_gcd.append(gcd(nums[i],mx[i]))

        prefix_gcd.sort()

        left=0
        right=n-1

        Sum=0
        while left < right:
            Sum+= gcd(prefix_gcd[left],prefix_gcd[right])
            left+=1
            right-=1

        return Sum



        
       