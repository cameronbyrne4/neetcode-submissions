class Solution:
    def countSubstrings(self, s: str) -> int:
        # treat each i as the start of an odd of (if dupe) even substr
        # add 1 for every time we can expand until we cannot

        def palExpander(l ,r):
            if l < 0 or r == len(s) or s[l] != s[r]:
                return 0
            else:
                return 1 + palExpander(l-1, r+1)
        count = 0
        for i in range(len(s)):
            count += palExpander(i,i)
            if i != len(s)-1 and s[i] == s[i+1]:
                count += palExpander(i, i+1)
        return count
