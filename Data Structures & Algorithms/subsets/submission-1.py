class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        No dupes, any order.

        This is the simplest backtracking ever brother

        All numbers are unique

        Either add and move on or just move on!
        '''

        out = []
        out.append([])
        cur = []

        def bt(i):
            if i == len(nums):
                if cur != []:
                    out.append(cur.copy())
                return
            
            cur.append(nums[i])
            bt(i+1)
            cur.pop()

            bt(i+1)
        bt(0)
        return out