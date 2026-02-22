class Solution(object):
    def binaryGap(self, n):
        
        binary_number=bin(n)[2:]
        previous_one=-1
        longest_distance=0

        for i in range(len(binary_number)):
            if binary_number[i]=='1':
                if previous_one!=-1:
                    longest_distance=max(longest_distance,i-previous_one)
                previous_one=i
        return longest_distance

       


       