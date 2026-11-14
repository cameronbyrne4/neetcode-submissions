class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        O(n^2) to try all as the starters

        gas[i] > cost[i] means we are safe with no leftovers. those are the potential candidates
        '''

        # brute force
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1

        fuel = 0
        start_idx = 0
        for i in range(n):
            fuel += gas[i]
            fuel -= cost[i]

            # if neg we reset that hoe
            if fuel < 0:
                fuel = 0
                start_idx = i + 1
        return start_idx