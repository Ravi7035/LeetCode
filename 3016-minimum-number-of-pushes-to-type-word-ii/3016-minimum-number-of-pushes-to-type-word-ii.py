class Solution(object):
    def minimumPushes(self, word):
        freq={}
        Total_cost=0

        for ch in word:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1

        sorted_frequencies=sorted(freq.values(),reverse=True)

        Total_cost=0
        for i,freq in enumerate(sorted_frequencies):
            cost=i//8+1
            Total_cost += freq*cost
        return Total_cost

