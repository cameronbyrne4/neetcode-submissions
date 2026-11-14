class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Elements added once --> either add / skip per i-th element
        - Stop if sum too high or if it will be too high
        - Stop if we at the end
        - Stop and append solution if sum works
        '''

        candidates.sort()
        print(candidates)
        output = []
        def dfs(i: int, cur_path: List[int], cur_sum: int) -> None:
            #print("Debug | i = ", i, ", path: ", cur_path, ", sum = ", cur_sum)
            if cur_sum == target:
                output.append(cur_path[:])
                return
            if i >= len(candidates):
                return  # doesn't have the proper sum by now -> kill run
            if cur_sum > target:
                return  # overshot -> kill
            
            '''
            Duplicates:
            - if add --> next one add + skip
            - if skip --> next one skip

            How to detect if added
            '''
            
            # Case 1: 
            cur_path.append(candidates[i])
            cur_sum += candidates[i]
            dfs(i+1, cur_path, cur_sum)
            cur_path.pop()
            cur_sum -= candidates[i]

            # Case 2: Skip allll the way to the next non-duplicate (adjust i accordingly)
            j=i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, cur_path, cur_sum)
            
            

        dfs(0, [], 0)
        return output