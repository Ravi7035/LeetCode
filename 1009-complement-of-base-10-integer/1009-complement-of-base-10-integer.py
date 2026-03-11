class Solution(object):
    def bitwiseComplement(self, n):
        binary_number=bin(n)[2:]
        binary_number=list(binary_number)
        for i in range(len(binary_number)):
            if binary_number[i]=="1":
                binary_number[i]="0"
            else:
                binary_number[i]="1"
        output=0
        for i in range(len(binary_number)-1,-1,-1):
            output+=(2**i)*int(binary_number[len(binary_number)-i-1])
        return output



        

        

     