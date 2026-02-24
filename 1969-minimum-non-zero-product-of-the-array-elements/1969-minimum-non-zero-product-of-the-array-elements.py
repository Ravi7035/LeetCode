class Solution(object):
    def minNonZeroProduct(self, p):

   
        MOD = 10**9 + 7
        
        M = pow(2, p) - 1        
        second = M - 1           
        exp = pow(2, p - 1) - 1  
        
        return (M * pow(second, exp, MOD)) % MOD
        