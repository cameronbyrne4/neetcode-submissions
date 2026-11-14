from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        Should we just do a counter??
        - Mathematically there are at most 2 solutions
        '''
        n = len(nums)
        limit = n//3    # must appear more than limit   
        output = []

        freq = Counter(nums)
        
        for key, val in freq.items():
            if val > limit:
                output.append(key)
            if len(output) == 2:
                break
        return output
            


