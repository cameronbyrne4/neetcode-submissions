class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        uniqueness determined by frequency?
        Can we sort a counter dict?

        sum the squares and compare?

        or we can just sort at he start idk

        Doesnt this feel like a backtracking / dfs problem?
            either repeat or go next

        we should skip dupes from nums

        '''
        out = []

        def bt(i: int, p: list[int], c: int):   # idx, path, sum
            if c == target and p:
                out.append(p[:])
                return
            if i == len(nums): # out of range
                return
            if (c) > target:  # too big
                return

            #skip or repeat
            
            #repeat
            n = nums[i]
            p.append(n)
            c += n
            bt(i, p, c)
            c -= n
            p.pop()

            #skip
            bt(i+1,p,c)


        bt(0, [], 0)
        return out