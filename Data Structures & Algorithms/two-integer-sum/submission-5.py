from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sorting is slower, so we will do linear time that uses more space

        # Dictionary:     Desired value --> idx
        d = defaultdict(int)
        for i, n in enumerate(nums):
            
            d[target-n] = i
        print(d)
        for i, n in enumerate(nums):
            if n in d:
                a,b = d[n], i
                if a==b:
                    continue    #cant be self
                if b < a:
                    a,b = b,a
                return [a,b]


