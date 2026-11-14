import math
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        First, use backtracking to find all working tuples
            - can use 0 or inf number of each num (until it's larger than target)

        Then have to find the number of unique PERMUTATIONS (n!) from each tuple:
            - Math?
            Permutations = n! / (f_1! * ... * f_n!)
        '''
        nums.sort() # quality of life
        count = 0

        def backtrack(i, cur_arr, cur_sum, cur_set): # cur_arr is just a LENGTH
            nonlocal count
            if i >= len(nums) or cur_sum + nums[i] > target:
                return
            
            # By this point, i is a valid index and the cursum is below target
            # We can stop if it's at target
            cur_sum += nums[i]
            cur_arr += 1
            cur_set[nums[i]] += 1
            if target == cur_sum:
                # Grow count using special conbination logic?
                # Count number of unique chars in cur_sum
                # This seems costly, Can we keep track with a dict or set?
                val = math.factorial(cur_arr)

                for v in cur_set.values():
                    val //= math.factorial(v)
                
                count += val
            
            

            # 1 --> added current and STAY
            backtrack(i, cur_arr, cur_sum, cur_set)

            # Reset
            
            cur_sum -= nums[i]
            cur_arr -= 1
            cur_set[nums[i]] -= 1
            if cur_set[nums[i]] == 0:
                del cur_set[nums[i]]    # trims length of dict
            # 2 --> SKIP AND MOVE ON
            backtrack(i+1, cur_arr, cur_sum, cur_set)
            


        backtrack(0, 0, 0, defaultdict(int))
        return int(count)