class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Seems just like the rainwater one

        Each rectangle is the min height times how many places right and left it can go while being at or above that height
        '''
        n = len(heights)
        lefts = [-1] * n

        # need to use some sort of stack to do these
        stack = []  # always decreasing, we can add the length of the stack?
        for i in range(n):
            # Pop when the top is too small. Our stack is always INCREASING
            # The prev value should be the idx of the value that is smaller than it
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                lefts[i] = stack[-1]    # index of where it is TOO SMALL AND WE HATE IT # DO NOT INCLUDE IN MATH
            stack.append(i)
            
        
        # rights
        max_area = 0
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # calc answer then append
                # todo
            cur = n
            if stack:
                cur = stack[-1]
                # Cur == index where it is too small DONT INCLUDE HIMMMMM
                # 1 2 3 4 5
            max_area = max(max_area, heights[i] * (cur-lefts[i] - 1))
            stack.append(i)


        return max_area