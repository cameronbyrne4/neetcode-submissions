class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        It's a decision tree

        At each stage we can add or not add a number (both to a sum and array)
        '''
        res = []        # List of lists
        nums.sort()
        def bt(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    # dont do this path 
                    continue
                else:
                    cur.append(nums[j])
                    bt(j, cur, total + nums[j])
                    cur.pop()

        bt(0,[], 0)
        return res