class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make prefix and suffix arrays
        # prefix[i] is the product up to and excluding i
        #
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        p = 1
        s = 1
        for i in range(n):
            prefix[i] = p
            p *= nums[i]
        for i in range(n-1,-1,-1):
            suffix[i] = s
            s *= nums[i]

        output = []
        for i in range(n):
            output.append(prefix[i] * suffix[i])
        return output

