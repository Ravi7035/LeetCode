class Solution(object):
    def beautifulSubsets(self, nums, k):
        nums.sort()
        result=[]
        frequency={}
        count=[0]
        def backtrack(start):
            if start==len(nums):
                return 
            for i in range(start,len(nums)):
                if frequency.get(nums[i]-k,0)>0:
                    continue
                frequency[nums[i]]=frequency.get(nums[i],0)+1
                count[0]+=1
                backtrack(i+1)
                frequency[nums[i]]-=1
                if frequency[nums[i]]==0:
                    del frequency[nums[i]]    
        backtrack(0)            
        return count[0]
                
            
           
      