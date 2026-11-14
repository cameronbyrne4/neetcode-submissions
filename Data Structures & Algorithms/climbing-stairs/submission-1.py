class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        bottom up  = Start at bottom of tree (base case)
        - track the number of ways to get to the current step
        '''
        # only need 2 variables that get shifted right with each calc
        cache = [1] * 2
        
        for i in range(n-1):
            temp = cache[0]
            cache[0] = cache[0] + cache[1]
            cache[1] = temp
        return cache[0]