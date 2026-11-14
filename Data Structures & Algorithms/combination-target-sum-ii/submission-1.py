class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()
        candidates.sort()
        # i = index in candidates, cur = current list of numbers, total = current sum of cur list
        def backtrack( i , cur, total):
            # end case one, the total is good
            if total == target:
                if frozenset(cur) in seen:
                    return
                seen.add(frozenset(cur))
                res.append(cur.copy())
                return

            # other end cases
            # -- Sum too high, or index too high
            if total > target or i >= len(candidates):
                return
            
            # Else: we have some choices to make

            # Case 1: add the current number
            cur.append(candidates[i])
            backtrack(i+1, cur, total + candidates[i])
            # Case 2: don't add the current number
            cur.pop()
            backtrack(i+1, cur, total)
        
        backtrack(0,[],0)
        return res


        # my current solution unfortunately does not sift out duplicates, uhh how do i do that.
        # we can use a set or a dict to store each completed one's frequencies