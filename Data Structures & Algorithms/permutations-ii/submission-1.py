class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        Lingo:
            - Permutation = order matters!
            - Could use some weird swapping algo
            - Either want to skip duplicates or track the output frequency dict... (-10 to 10)

        Idea:
            for each index i we can swap with the index j (i+1 to end)
            only if j != i
            append to answer every time
        '''

        nums.sort()
        out = []
        cur = nums.copy()
        seen = set()
        def bt(i):
            #print(i, cur)
            if tuple(cur) not in seen:
                out.append(cur.copy())
                seen.add(tuple(cur))

            if i == len(nums):
                return
            for j in range(i+1, len(nums)):
                #print("comparing i and j:", i, j)
                if cur[i] != cur[j]:
                    #print("Swap")
                    cur[i], cur[j] = cur[j], cur[i]
                    bt(i+1)
                    cur[i], cur[j] = cur[j], cur[i]
                    bt(i+1)
                    

        bt(0)
        return out



