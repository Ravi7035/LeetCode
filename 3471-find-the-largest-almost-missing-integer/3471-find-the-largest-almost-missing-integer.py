class Solution(object):
    def largestInteger(self, nums, k):
        
        freq={}

        current_window=nums[:k]
        for num in set(current_window):
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1

        left=1

        for right in range(k+1,len(nums)+1):
            current_window=nums[left:right]
            
            for num in set(current_window):
                if num not in freq:
                    freq[num]=1
                else:
                    freq[num]+=1

            left+=1

        largest=-1
        for num in freq:
            if freq[num]==1:
                if num > largest:
                    largest=num

        return largest


        




  