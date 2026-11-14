class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Initial idea:
            just store it as val --> freq
            then at the end sort by the 2nd thing to find the max
            its like O(nlogn)
        '''
        # Bucket sort algo?

        # find counts
        count = Counter(nums)

        # place in buckets for the count
        buckets = [[] for _ in range(len(nums) + 1)]

        for c in count:
            buckets[count[c]].append(c)

        # Go backwards over my buckets until res is length k
        res = []
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res




        return res



   