class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        doing all combos
        - last time it was either Y or N for each number
        - now we can add it however many times we want..
        - stop once we get above the target i present
        - options: add i, or any other number
        '''
        
        result = []
        subset = []
        
        def dfs(i, sum, t):
            
            print("sum is", sum)
            if sum > t:
                return
            if sum == t:
                result.append(subset.copy())
                return

            # if we aren't at target yet we add any of the numbers
            
            # some problem over here!!!!!
            for n in range(i, len(nums)):
                subset.append(nums[n])
                print("calling dfs AGAIN on: ", subset)
                dfs(n, sum + nums[n], t)
                subset.pop()
                
            
        dfs(0,0, target)
        return result

            # subset.pop()  NOTE: not including this I dont think since we won't add []