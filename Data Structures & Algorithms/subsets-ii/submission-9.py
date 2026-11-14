class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Retuning all subsets we explore

        Note: no duplicates in terms of frequency
            - Cannot just compare sums

        Idea:
            - maybe we can sort then skip dupes somehow?
            - like for n dupes we add them 0 to n times to the subarray
        '''

        nums.sort()
        out = []    # literally add every substring we can find

        def dfs(i, cur_list):
            # append every single time
            

            if i >= len(nums):
                out.append(cur_list[:])
                return  # dead end, we are done
            
            # count dupes
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            # By the end, j is at a non-duplicate or is past the end of the list

            # prepare to dfs after adding 0,1,..,n duplicates (j-i >= 1  always)
            # Case 0: add nothin
            for k in range(0,j-i+1):    # 1,2,...
                # add k dupes, run (after j), remove k dupes
                for _ in range(k):
                    cur_list.append(nums[i])
                dfs(j, cur_list)
                for _ in range(k):
                    cur_list.pop()
                



        dfs(0, [])
        return out