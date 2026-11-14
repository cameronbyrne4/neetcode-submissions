class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        This sounds like I need to form a trie and return the height something using height

        nvm, LC easy is just a search 
        '''

        i = 0
        res = ""
        # increment i over and over
        # stop if the i == words length bc then we have to be done
        # and stop if character is not the same
        while True:
            if i == len(strs[0]):
                return res
            char = strs[0][i]       # all must match this

            for s in range(1, len(strs)):
                if i >= len(strs[s]):
                    return res
                if char != strs[s][i]:
                    return res
            i += 1
            res += char

       