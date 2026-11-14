class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        Doing sets of operations
            - max between two triples 

        Idea should be easy
        '''
        a,b,c = 0, 0, 0
        t1,t2,t3 = target[0], target[1], target[2]

        for x,y,z in triplets:
            # 3 bases to cover
            if x == t1 and y <= t2 and z <= t3:
                a = 1
            if y == t2 and x <= t1 and z <= t3:
                b = 1
            if z == t3 and x <= t1 and y <= t2:
                c = 1

        return a == b == c == 1