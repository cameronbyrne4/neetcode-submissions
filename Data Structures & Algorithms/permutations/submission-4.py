class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        We can just have an endless loop, stopping when the thing is full instead of at final index?

        How do we ensure not the repeat? keep a set of idx or ints?

        Must pick some element -> no inf loop
        '''

        out = []
        n = len(nums)
        unused = [0] * n # used if 1
        cur = []
        def bt(i):
            if min(unused) != 0:
                out.append(cur.copy())
            # print(unused)
            for j in range(n):
                print(f"cur={cur}, unused={unused}")
                # only do the ones that are still unused == 0
                if unused[j] == 1:
                    continue
                unused[j] = 1
                cur.append(nums[j])
                bt(i+1)
                cur.pop()
                unused[j] = 0

        bt(0)
        return out
