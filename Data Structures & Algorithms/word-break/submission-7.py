class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        '''
        n = len(s)
        dp = [False] * (n+1)    # dp[i] True if the s[i-1] is fulfillable
        dp[0] = True

        for i in range(n+1):
            if dp[i] == False:
                continue
            
            # dp[i] reachable, so s[i-1] valid
            for word in wordDict:
                print("checking: ", word)
                # if all the characters match in the string we are okay
                # Should we do two pointer? sure
                l1 = i # pointing to s
                l2 = 0  # pointing to word
        
                while l1 < len(s) and l2 < len(word) and s[l1] == word[l2]:
                    print("comparing:, ", s[l1], word[l2])
                    l1 += 1
                    l2 += 1
                if l2 == len(word):
                    dp[l1] = True
        print(dp)
        return dp[n]