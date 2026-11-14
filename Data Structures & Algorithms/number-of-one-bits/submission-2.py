class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(1) means I cant just count them iteratively
        res = 0
      
        for i in range(32): #32 times
            if (1 << i) & n > 0:
                res += 1
            
        return res
