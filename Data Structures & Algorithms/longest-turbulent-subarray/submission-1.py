class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        - challenge = judging if next element is ok

        - if ok, up count and conitnue

        - if not, check count with max, reset count, and reset subarray

        - at end add whatever we got
        '''
        out = 1
        cur = 1
        for r in range(1, len(arr)):
            # cur always gotta be 2
            
            
            # If valid, kee counting
            if (arr[r] > arr[r-1] and arr[r-2] > arr[r-1]) or (arr[r] < arr[r-1] and arr[r-2] < arr[r-1]):
                cur += 1
                print("Count up!", cur, "at number ", arr[r])
            else:
                out = max(out, cur)
                if arr[r] == arr[r-1]:
                    cur = 1
                else:
                    cur = 2 # contains only the one that just failed
                print("Reset count at", arr[r])

        out = max(out, cur)
        return out