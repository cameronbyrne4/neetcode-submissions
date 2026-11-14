class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Finding length of longest substr (no dupes)

        Solution:
        - Move a pointer over the string
        - each character:
            - if it's already in the set, DONT ADD YET
                - Move the left pointer until its not!
        '''
        # "zxyzxyz"
        seen = set()
        res = 0
        l = 0
        for r in range(len(s)):

            # Fix the dupes
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            # Array will follow the rules by now
            res = max(res, (r-l+1))
        return res
        