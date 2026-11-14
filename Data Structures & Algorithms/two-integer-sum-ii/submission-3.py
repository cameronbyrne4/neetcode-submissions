class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Increasing like 1,1,1,2,3,4,4,4,5
        l,r = 0, len(numbers)-1

        while l < r:
            # always one solution btw so no fallback
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
