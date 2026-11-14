from collections import defaultdict
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Can we just swap all n nodes with whatever is k % n index away?

        or not a swap but just update the new index? idk man
        """
        idxs = defaultdict(int)
        
        for i, n in enumerate(nums):
            idxs[i] = n
        
        # We will reconstruct nums in place
        for key, val in idxs.items():    # key is the old idx before rotations
            nums[(key+k)%len(nums)] = val

        return nums

        