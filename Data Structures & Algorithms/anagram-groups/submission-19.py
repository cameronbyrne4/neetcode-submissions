from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - input: list of strings
        - output: list of lists of strings with same freq maps

        Solution:
        store in hash map where key is the frequency as chars array

        TIPS:
        1. learn ord()
        2. use tuple to hash, not an array or hash

        '''
        hm = defaultdict(list)
        result = []
        # Create hash for each input string and put into table
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')] +=1
            hm[tuple(freq)].append(s)

        # turn hash map into list list
        for f, l in hm.items():
            curarr = []
            for w in l:
                curarr.append(w)
            result.append(curarr)
        return result
