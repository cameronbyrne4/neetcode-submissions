from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        just make a counter and return the backwards values?

        of dict(set), where key is the count, no thats n^2

        Heap?

        sort then max heap?

        counter then buckets (second conters)
        '''
        nums = Counter(nums)

        # invert counter
        freqs = defaultdict(list)

        for n,c in nums.items():
            freqs[c].append(n)  # uh but this isnt sorted tho right

        freqs = dict(sorted(freqs.items(), reverse = True))

        res = []

        for listy in freqs.values():
            for j in listy:   # list of numbers
                res.append(j)
                if len(res) == k:
                    return res

        

