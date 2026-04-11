class Solution(object):
    def minimumDistance(self, nums):
        min_dist=float('inf')
        freq={}

        for index,number in enumerate(nums):
            if  number not in freq:
                freq[number]=[]
            freq[number].append(index)

        for indices in freq.values():
            if len(indices) >=3:
                for i in range(len(indices)-2):
                    min_dist=min(min_dist,2*(indices[i+2]-indices[i]))
        return min_dist if min_dist != float('inf') else -1
              
        
        
        