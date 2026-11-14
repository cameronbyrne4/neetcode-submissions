class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        BRUTE FORCE: count up from each index

        in order
        -- check the next number in arr
                -- reset count while we at it
        -- if it's smaller or equal -> add to the stack
        -- if it's larger -> start popping until its NOT, 
            then add it to the stack


        '''

        result = [0] * len(temperatures)
        stack = [] # pairs of i, t
        for i in range(len(temperatures)):
            # while new kid's temp is larger, we back ts up via pop
            while stack and stack[-1][1] < temperatures[i]:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            # Now that new kid is smaller or equal, we add him to stack
            stack.append((i, temperatures[i]))
            
        return result