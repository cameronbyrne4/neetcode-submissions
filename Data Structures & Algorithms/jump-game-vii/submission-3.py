class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        '''
        you can jump to the 0's in ur range

        Greedy = take the biggest jump possible. 

        For reverse:
            if true:
                mark as next starting point

        '''
        n = len(s)
        # print("n is ", n)
        dp = [0] * n    # dp[i] means we can or cannot (0,1) jump to s[i]
        dp[0] = 1       # start on idx 1
        
        for i in range(n):
            # print("i: ", i)
            if s[i] == "0" and dp[i] == 1:
                for j in range(i+minJump, 1 + min(i+maxJump, n-1)):
                    # print("     j: ", j)
                    if s[j] == "1" or dp[j] == 1:
                        continue
                    
                    # Valid start and confirmed reachable:
                    dp[j] = 1

        return True if dp[n-1]==1 else False

        