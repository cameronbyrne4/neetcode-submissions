class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Backtracking IS ALL ABOUT DECISION TREES

        NUMBERS ARE DISTINCT 

        WE CAN HAVE DUPES

        SO BASICALLY EVERY NUMBER SMALLER THNA TARGET CAN BE FILLED LIKE X*Y*Z*

        Either:
            1. add another of the curernt number
            2. move onto the next number

        Stop when:
            1. over target
            2. at target!
        '''

        res = []
        def dfs(i, cur, s):
            # BASE CASES
            if s == target:
                res.append(cur.copy())
                return
            if s > target or i > len(nums)-1:
                return
            
            # BACKTRACK
            # Case 1 WE DO ADD THIS ONE
            cur.append(nums[i])
            dfs(i, cur, s + nums[i])
            cur.pop()
            # CASE 2 WE DONT ADD IT
            dfs(i+1, cur, s)



        dfs(0, [], 0)      # 0 is the index in the nums arr
        return res