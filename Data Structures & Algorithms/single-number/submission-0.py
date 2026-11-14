class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR is ^
        # 0011 ^ 0011 = 0000
        # 0011 0101 0101 0001 0011 = 0110 0101 0001 0011 = 0011 0001 0011 - 0010 0011 = 0001
        # how the fuck am i supposed to know it translating
        res = 0
        for i in nums:
            res ^= i
        return res