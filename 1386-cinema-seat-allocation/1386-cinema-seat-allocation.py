class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):

        hash_map={}

        for row,seat in reservedSeats:
            if row not in hash_map:
                hash_map[row]=set()

            hash_map[row].add(seat)
        
        count=(n-len(hash_map))*2

        for row in hash_map:
            reserved=hash_map[row]

            left=all(seat not in reserved for seat in [2,3,4,5])
            middle =all(seat not in reserved for seat in [4,5,6,7])
            right=all(seat not in reserved for seat in [6,7,8,9])

            if left and right:
                count+=2

            elif left or middle or right:
                count+=1

        return count
            
            


    
    


      