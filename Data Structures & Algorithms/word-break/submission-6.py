class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # can loop through characters in s
        # adding chars to a subarray
        # search in a hash every time to see if that subarray is in the dic
        # if it is, then we reset the subarray?
        
        '''
        No that won't work:
        * say the word is "cats" and our bank has "ca" and "cats"
        * would get stopped at ca... we need to think recursively

        I'm going to think like counting coins, where they r all False to beginn
        For each i in s:
            We go through each word in the worddict (that's short enough)
            we update to true if one of them connects (starting at index that is word length behind)
            * count backwards
            * make sure back one is true (or its the start)
            * then count characters forwards
            * update true if we make it all teh way
        '''
        n = len(s)
        m = len(wordDict)
        dp = [False] * (n+1) # length of the string has indices 0 to n
        dp[0] = True
        print(dp[0])
        for i in range(1,n+1):
            for word in wordDict:
                # confirm we can try forming branch
                if s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True

            print(dp[i])
        return dp[-1]