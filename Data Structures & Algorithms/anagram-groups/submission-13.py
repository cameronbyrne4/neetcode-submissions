class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        make a hash map where the key is the anagram (or the sorted string)

        Key is the anagram as a alphabetical


        '''

        graph = defaultdict(list)


        for s in strs:
            key = "".join(sorted(s))        # This splits it up into list then sorts
            graph[key].append(s)
        
        res = []
        for v in graph.values():
            res.append(v)
        return res
