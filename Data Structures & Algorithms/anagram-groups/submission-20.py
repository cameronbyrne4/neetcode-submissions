class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        All are lowercase btw
        '''

        d = defaultdict(list)      # key is the array, value is the list of words
        for s in strs:
            count = [0] * 26  # turn to tuple later
            for c in s:
                count[ord(c)-ord('a')] += 1
            
            d[tuple(count)].append(s)
        
        out = []
        for m,i in d.items():
            out.append(i)
        
        return out