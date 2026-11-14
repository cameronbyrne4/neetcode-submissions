class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        Trust is directional

        find whoever trust value is n-1 (n-1 people trust them)
        '''
        counts = defaultdict(int)

        for t in trust:
            counts[t[0]] -= 1       # Trust people (not judgelike)
            counts[t[1]] += 1       # is trusted (judgelike)

        for k,v in counts.items():
            if v == n-1:
                return k
        return -1
        
        