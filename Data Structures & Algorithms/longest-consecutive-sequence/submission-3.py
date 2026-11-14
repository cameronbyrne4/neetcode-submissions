class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        * sequence = 1 greater
        * dont need to in original
        * Cannot sort (too slow)
        - can't just record the min and look for +1
        - I think we should see if the number below it is in our hash (all start at 1),
            then on the number below, add the current consecutive nums stored at the num above
        - then return the max of the hash

        Hint 2: we can identify starts of sequence as having no predecessor (n-1 not found)
        '''

        # Convert array to a hash set
        hash_table = {}
        for num in nums:
            hash_table[num] = 1

        # Label the sequence starts with 2
        for num in nums:
            if hash_table.get(num-1) is None:
                hash_table[num] = 2

        maxSequenceLen = 0
        for num in nums:
            if hash_table[num] == 2:
                # For all the starts we can count
                sequenceLen = 1
                i = num
                while hash_table.get(i+1) is not None:
                    sequenceLen += 1
                    i += 1
                maxSequenceLen = max(maxSequenceLen, sequenceLen)

        return maxSequenceLen